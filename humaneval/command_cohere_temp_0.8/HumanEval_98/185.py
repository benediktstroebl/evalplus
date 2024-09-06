Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function defines a set of uppercase vowels and then uses a loop to iterate through the characters of the input string s. It checks if the character is uppercase and belongs to the set of uppercase vowels. If it does, and the character is in an even index (checked using the modulo operation), it increments the count variable. Finally, it returns the accumulated count.

This solution should be able to handle all test cases, including edge cases, and follows the requirement of being self-contained. 
If you'd like you can also introduce a unittest block to properly test the function with a variety of inputs. This would improve the solution's organization and robustness. Here's an example of how you can test this function:
```python
import unittest

def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count

class TestCountUpper(unittest.TestCase):
    def test_count_upper_abcde(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_abcdefg(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_count_upper_ddbb(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_count_upper_iiooo(self):
        self.assertEqual(count_upper('IIOOO'), 2)

if __name__ == '__main__':
    unittest.main()
```

This way, running the script will now execute the unit tests, assessing the function's correctness in multiple scenarios.