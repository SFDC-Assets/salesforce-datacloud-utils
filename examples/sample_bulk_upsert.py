from salesforce_datacloud_utils import SalesforceDataCloud

sfdc=SalesforceDataCloud()
sfdc.bulk_upsert("Event_API", "runner_profiles", ["bulk_test.csv"])

