Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case, and then returns the set's length to provide the number of distinct characters.

Here's the markdown code block with the corresponding problem and solution:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    characters = set(string.lower())
    return len(characters)
```
This code demonstrates how to solve the problem of counting distinct characters in a string using a self-contained Python function.