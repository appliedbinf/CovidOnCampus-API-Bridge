# CovidOnCampus API Bridge

In order to ensure end to end encryption of scheduling data, we make use
of a serverless function to bridge API callbacks.

The serverless function is configured to run on the AWS/Lambda gateway, using
a provisioned certificate.  Deployed via zappa 