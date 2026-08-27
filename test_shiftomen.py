# test_shiftomen.py
"""
Tests for ShiftOmen module.
"""

import unittest
from shiftomen import ShiftOmen

class TestShiftOmen(unittest.TestCase):
    """Test cases for ShiftOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShiftOmen()
        self.assertIsInstance(instance, ShiftOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShiftOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
