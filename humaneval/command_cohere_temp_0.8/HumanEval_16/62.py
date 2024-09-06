Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase and then uses the `set` data structure to automatically filter out duplicate characters. Then it returns the count of distinct characters as the length of the `set` data structure.

Here is the entire code block including the function and example tests:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of """
    characters = set(string.lower())
    return len(characters)

# Test Cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```