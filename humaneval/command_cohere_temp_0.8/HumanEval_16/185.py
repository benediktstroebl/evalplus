Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case, and then returns the set's length to provide the number of distinct characters.

To apply this function to test cases, the script should include the import statement `'pytest'` and then create corresponding test functions annotated with `@pytest.mark.unittest`. For example:
```python
import pytest

def test_count_distinct_characters_with_lowercase(self):
    """Test for lowercase strings"""
    assert count_distinct_characters("xyzXYZ") == 3

def test_count_distinct_characters_with_mixed_case(self):
    """Test for mixed-case strings"""
    assert count_distinct_characters("Jerry") == 4
```
Here's the expected complete script with the above function and test cases:
```python
import pytest

def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)

def test_count_distinct_characters_with_lowercase(self):
    """Test for lowercase strings"""
    assert count_distinct_characters("xyzXYZ") == 3

def test_count_distinct_characters_with_mixed_case(self):
    """Test for mixed-case strings"""
    assert count_distinct_characters("Jerry") == 4

```
To run the tests, use the command `pytest` in your terminal, and it will automatically execute the test functions and report any failures or errors.