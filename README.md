# Automated Marketing Campaign Request and Lead Generation/Management
The journey begins with the user submission of index.html
Upon submission a POST call is made to a Zapier webhook with the form data in json body. 
A Jira issue is created in the "Marketing Campaigns Project"
Based on the Campaign Type (specifies region) an email is sent to the requesting party, and a slack message is delivered to the specific team channel(s). 
When the Jira issue goes from status "Approving" to "Done", a zapier webhook receives a POST request, runs index.py. 
This program creates a Jira Project which creates a Lead Generation/Management template. 
When a user responds to a CTA with the associated campaign a lead (issue) is created. 
The status is responsivwe to vaerious statuses that exist within the NEXUS API (note submissions field changes, etc.). 
When the lead is closed it's closed as "Won" or "Lost". 
