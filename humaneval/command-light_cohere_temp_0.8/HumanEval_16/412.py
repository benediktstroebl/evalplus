```python
def count_distinct_characters(string: str):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    return len([char for char in string.lower() if char.isupper() == char.islower()])
 straightforwardly, but it handles all characters without considering case sensitivity.

```