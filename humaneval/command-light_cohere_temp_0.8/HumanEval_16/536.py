```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    A set of characters is created without case sensitivity, and the length of this set is returned.
"""
    import re
    # Define a regex pattern to match any character
    pattern = r'[^\W\d]'
    # Use the regex to find all matches in the string
    all_matches = re.findall(pattern, string)
    return len(all_matches)
```