# test_codevault.py
"""
Tests for CodeVault module.
"""

import unittest
from codevault import CodeVault

class TestCodeVault(unittest.TestCase):
    """Test cases for CodeVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeVault()
        self.assertIsInstance(instance, CodeVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
