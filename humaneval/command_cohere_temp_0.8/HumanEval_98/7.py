```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count of uppercase vowels in even indices
    count = 0
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the current character is an uppercase vowel
        if char.isupper() and char in vowels and (i % 2 == 0):
            count += 1
    # Return the count of uppercase vowels in even indices
    return count
```

The script defines a function `count_upper()` which counts the number of uppercase vowels in even indices of a given string and returns the count. It first defines the vowels to be checked, initializes the count to 0, then iterates through each character in the string, and increments the count if the character is an uppercase vowel and its index is even. Finally, it returns the total count. 

The unit tests for this problem could be as follows:
```python
import unittest

def test_count_upper():
    # Test case 1: Count uppercase vowels in even indices
    assert count_upper('aBCdEf') == 1

    # Test case 2: Count should be zero for strings without uppercase vowels or even indices
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0

    # Test case 3: Count multiple occurrences
    assert count_upper('AAcckkEEeeDD') == 4

    # Test case 4: Count should not consider non-vowels
    assert count_upper('aBCdei') == 1

class TestSuite(unittest.TestCase):
    def test_count_upper(self):
        assert count_upper('aBCdEf') == 1

    def test_count_upper_with_multiple_occurrences(self):
        assert count_upper('AAcckkEEeeDD') == 4

    def test_count_upper_with_odd_indices(self):
        assert count_upper('aBCdei') == 1

    def test_count_upper_with_no_uppercase_vowels(self):
        assert count_upper('abcdefg') == 0

    def test_count_upper_with_no_even_indices(self):
        assert count_upper('dBBE') == 0

if __name__ == '__main__':
    unittest.main()
```

This test suite covers different scenarios, including testing for multiple occurrences, non-vowels, odd indices, and cases where there are no uppercase vowels or even indices.