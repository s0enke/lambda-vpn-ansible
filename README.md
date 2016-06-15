# Execute Ansible on Home Servers via Lambda

# Problem

Home servers (RaspberryPis running e.g. Mopidy, or Smarthome stuff)
should be kept up-to-date by regular Ansible converge runs. 

Ansible runs should be possible on a event-based schedule, so we need push.

Multiple home networks are involved. They can be reached via VPN (FritzBox).

## Solution

 - a Lambda function which starts a disposable EC2 instance
 - this instance creates a VPN tunnel and executes Ansible
 - the instance terminates after the Ansible execution

## Implementation

 - Gordon is used for Lambda provisioning

## TODO

 - regular execution via CloudWatch events
 - lookups for security groups?
 - Ansible
 - Metrics and Alarms
