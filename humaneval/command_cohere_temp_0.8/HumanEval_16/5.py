Here's a Python script that contains a function called `count_distinct_characters` which accepts a string and returns the number of distinct characters within the string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The above function leverages Python's built-in `set` to remove duplicate characters, and the `lower()` method to normalize all characters to lowercase. This ensures that characters like 'x', 'X', and 'xX' are all treated as the same character. The `len()` method then returns the number of unique characters in the set. 

To ensure the function performs as expected on different inputs, here are some test cases to include in a separate file, e.g., test_count_distinct_characters.py:
```python
import unittest
from count_distinct_characters import count_distinct_characters # assume this function is defined in a file named count_distinct_characters.py

class TestCountDistinctCharacters(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_different_case(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_mixed_string(self):
        self.assertEqual(count_distinct_characters('Aa123$%^{}[]:-=<>/?@[:,.!') , 12)

if __name__ == '__main__':
    unittest.main()
```
This script will ensure the function works correctly for different cases, and the output is correct for the given inputs. 
If the script is in a different file, make sure to execute the script with the `python -m unittest test_count_distinct_characters` command to run the tests. 
The `python -m unittest` is a command-line program that loads the built-in unittest module and executes the test cases. 
The `test_count_distinct_characters` is the name of the file and the Python function that executes the tests. 
This should be the command to run the test if the script is in a file called test_count_distinct_characters.py:
```bash
python -m unittest test_count_distinct_characters
``` 
This command executes the test cases and displays a summary of the results, detailing the number of tests that passed, failed, or raised errors.  In this case, it is better to see the outcome of the test runs to ensure the function behaves as expected.  If the outcome is "OK", then all tests have passed correctly.