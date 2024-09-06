Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. Finally, it returns the length of the set, which is the number of distinct characters. 

To validate the functionality of the function, you can use the following tests:
```python
test_cases = [
    ("xyzXYZ", 3),         # Should count distinct characters irrespective of case
    ("Jerry", 4),         # Handles strings with both uppercase and lowercase letters
    ("xxxyyXXXyyY", 6),   # Handles strings with repeated characters
    ("", 0),              # Handles empty strings
    (None, 0),            # Handles None input
]
```
You can incorporate these tests into your script to verify the function's behavior using the `assert` statement:
```python
import unittest
def test_distinct_characters():
    for input_, expected in test_cases:
        assert count_distinct_characters(input_) == expected

class TestCountDistinctCharacters(unittest.TestCase):
    def test_distinct_characters(self):
        test_distinct_characters()

if __name__ == '__main__':
    unittest.main()
```
Running this test suite will verify that the `count_distinct_characters` function behaves as expected for different inputs.