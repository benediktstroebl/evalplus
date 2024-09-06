```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len(set(string.lower()))
```

Here is a self-contained Python function that counts the number of distinct characters in a given string, regardless of case. It uses the set() and `lower()` methods to achieve this and returns the number of distinct characters.

The function passes all the test cases provided in the initial prompt. 

Let me know if there is anything else I can help you with!