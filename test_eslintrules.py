# test_eslintrules.py
"""
Tests for ESLintRules module.
"""

import unittest
from eslintrules import ESLintRules

class TestESLintRules(unittest.TestCase):
    """Test cases for ESLintRules class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ESLintRules()
        self.assertIsInstance(instance, ESLintRules)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ESLintRules()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
