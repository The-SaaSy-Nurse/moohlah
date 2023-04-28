import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
from jira import JIRA
from flask import Flask, request

def read_counter():
    with open("counter.txt", "r") as file:
        return int(file.read().strip())

def update_counter(new_value):
    with open("counter.txt", "w") as file:
        file.write(str(new_value))

def create_jira_project(z, bundle):
    try:
        url = "https://itsnursebee.atlassian.net/rest/api/2/project"
        auth = HTTPBasicAuth("tim.hunter@nursebee.com", "ATATT3xFfGF09Q0xErm41zPzo3RvFCGzGAsdnuCX6MG53oEhl937PMWYJvfcbpgoMNhWlvhL7Hd5XChdFqD8FE0dI32FoAT9upydSJWdZhJpaWLZF_s05psDKdgZJANxNnXpcACY5RG7eRJXf5dY79tEFJyz1Uvshws2CPvxSyW1OUeQhdhB5R0=4B2D521E")
        today = datetime.today()
        counter = bundle['meta']['counter'] if 'counter' in bundle['meta'] else 1
        project_name = f"My Project {today.year}-{today.month}-{today.day}-{counter}"
        project_key = f"CMP{counter}"
        project_type_key = "business"
        project_template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"
        project_lead_account_id = "6421d42ff1b529dfa98e55f6"
        project_description = "Cloud migration initiative"
        project_avatar_id = 10412
        project_category_id = 10000
        project_permission_scheme = 0
        project_notification_scheme = 10000
        project_issue_security_scheme = 10000
        project_assignee_type = "PROJECT_LEAD"
        project_url = "http://nursebee.com"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "key": project_key,
            "name": project_name,
            "projectTypeKey": project_type_key,
            "projectTemplateKey": project_template_key,
            "leadAccountId": project_lead_account_id,
            "description": project_description,
            "avatarId": project_avatar_id,
            "categoryId": project_category_id,
            "permissionScheme": project_permission_scheme,
            "notificationScheme": project_notification_scheme,
            "issueSecurityScheme": project_issue_security_scheme,
            "assigneeType": project_assignee_type,
            "url": project_url
        }
        response = requests.post(url, json=payload, headers=headers, auth=auth)
        if response.status_code != 201:
            print(f"Response content: {response.content}")
        response.raise_for_status()
        counter += 1
        return {"project_key": project_key, "project_name": project_name, "counter": counter}
    except Exception as e:
        print(f"Error occurred while creating Jira project: {e}")
        raise e

def get_trigger_definition():
    return {
        'key': 'create_jira_project',
        'noun': 'Jira Project',
        'display': {
            'label': 'Create Jira Project',
            'description': 'Creates a new Jira project.'
        },
        'operation': {
            'perform': create_jira_project,
            'can_paginate': False
        }
    }

def read_counter():
    with open("counter.txt", "r") as file:
        return int(file.read().strip())

def update_counter(new_value):
    with open("counter.txt", "w") as file:
        file.write(str(new_value))

def create_jira_project(z, bundle):
    try:
        url = "https://itsnursebee.atlassian.net/rest/api/2/project"
        auth = HTTPBasicAuth("tim.hunter@nursebee.com", "ATATT3xFfGF09Q0xErm41zPzo3RvFCGzGAsdnuCX6MG53oEhl937PMWYJvfcbpgoMNhWlvhL7Hd5XChdFqD8FE0dI32FoAT9upydSJWdZhJpaWLZF_s05psDKdgZJANxNnXpcACY5RG7eRJXf5dY79tEFJyz1Uvshws2CPvxSyW1OUeQhdhB5R0=4B2D521E")
        today = datetime.today()
        counter = bundle['meta']['counter'] if 'counter' in bundle['meta'] else 1
        project_name = f"My Project {today.year}-{today.month}-{today.day}-{counter}"
        project_key = f"CMP{counter}"
        project_type_key = "business"
        project_template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"
        project_lead_account_id = "6421d42ff1b529dfa98e55f6"
        project_description = "Cloud migration initiative"
        project_avatar_id = 10412
        project_category_id = 10000
        project_permission_scheme = 0
        project_notification_scheme = 10000
        project_issue_security_scheme = 10000
        project_assignee_type = "PROJECT_LEAD"
        project_url = "http://nursebee.com"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "key": project_key,
            "name": project_name,
            "projectTypeKey": project_type_key,
            "projectTemplateKey": project_template_key,
            "leadAccountId": project_lead_account_id,
            "description": project_description,
            "avatarId": project_avatar_id,
            "categoryId": project_category_id,
            "permissionScheme": project_permission_scheme,
            "notificationScheme": project_notification_scheme,
            "issueSecurityScheme": project_issue_security_scheme,
            "assigneeType": project_assignee_type,
            "url": project_url
     }
        response = requests.post(url, json=payload, headers=headers, auth=auth)
        if response.status_code != 201:
            print(f"Response content: {response.content}")
        response.raise_for_status()
        counter += 1
        return {"project_key": project_key, "project_name": project_name, "counter": counter}
    except Exception as e:
        print(f"Error occurred while creating Jira project: {e}")
        raise e

def get_trigger_definition():
    return {
        'key': 'create_jira_project',
        'noun': 'Jira Project',
        'display': {
            'label': 'Create Jira Project',
            'description': 'Creates a new Jira project.'
        },
        'operation': {
            'perform': create_jira_project,
            'can_paginate': False
        }
    }


app = Flask(__name__)

@app.route('/https://84f6-136-36-74-200.ngrok-free.app', methods=['POST'])
def handle_webhook():
    try:
        result = create_jira_project(None, {"meta": {}})
        print(f"Jira project created: {result}")
        return "Jira project created", 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return f"Error occurred: {e}", 500

if __name__ == "__main__":
    try:
        result = create_jira_project(None, {"meta": {}})
        print(f"Jira project created: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")
    app.run(host='0.0.0.0', port=5000)
