Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in a given string, 
    ignoring case.
    Args: 
        string (str): input string

    Returns: 
        int: number of distinct characters
    """
    import re
    char_count = len(re.findall(r'[([ alphabetic ] for alphabetic in string.
    return len(set(char_count, str.
(c) == c.lower() for c in string))
```
Do you require additional help with this code?