```python
def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in the given string, regardless of case.
    Return the number of distinct characters.
    """
 complex implementation: uses the `set()` function to identify uniqueness.
#### Example test cases: 
- Test 1: 
Given 'xyzXYZ'
Return: 3
- Test 2: 
Given 'jerry'
Return: 4
"""
    return len(set(string.ascii()))
```