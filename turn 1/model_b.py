import unittest

class TestDataSharingAgreement(unittest.TestCase):
    def setUp(self):
        # Initialize the data sharing agreement with a set of initial fields
        self.agreement = {
            'data_type': 'customer_data',
            'sharing_partners': ['partner_a', 'partner_b'],
            'access_period': '3 months',
            'data_purposes': ['marketing', 'analytics'],
        }

    def test_agreement_flexibility(self):
        # Test if the agreement allows for adding new fields dynamically
        self.agreement['new_field'] = 'some_value'
        self.assertIn('new_field', self.agreement)

    def test_agreement_conformance_to_required_fields(self):
        # Test if the agreement contains all the required fields
        required_fields = ['data_type', 'sharing_partners', 'access_period', 'data_purposes']
        for field in required_fields:
            self.assertIn(field, self.agreement, msg=f"Missing required field: {field}")

    def test_agreement_conformance_to_data_type_values(self):
        # Test if the 'data_type' field has valid values
        valid_data_types = ['customer_data', 'sensitive_data', 'internal_data']
        self.assertIn(self.agreement['data_type'], valid_data_types, msg="Invalid data type")

    def test_agreement_conformance_to_sharing_partners_type(self):
        # Test if the 'sharing_partners' field is a list
        self.assertIsInstance(self.agreement['sharing_partners'], list, msg="'sharing_partners' must be a list")

    def test_agreement_conformance_to_access_period_format(self):
        # Test if the 'access_period' field is in the expected format (e.g., '3 months', '1 year')
        import re
        pattern = r'\d+ (months|years)'
        self.assertTrue(re.match(pattern, self.agreement['access_period']), msg="Invalid access period format")

if __name__ == '__main__':
    unittest.main()
