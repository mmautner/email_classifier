email_classifier
================

An email "importance" classifier, trained off of gmail data

Given as a talk at the [Boston Data Mining](http://www.meetup.com/Boston-Data-Mining/events/162468602/) Meetup group.

Pull requests are welcome.

Install the requisite python libraries first:

    shell$> pip install -r requirements.txt

Handling of inbound emails can be solved a number of ways--for the talk, I setup a Mailgun account to route forwarded 
emails from my Gmail account to an EC2 instance via HTTP rather than SMTP.

The receptor.py Flask app loads the classifier and feature vectorizer, extract the features from inbound emails 
and classify whether the email is important or not.
