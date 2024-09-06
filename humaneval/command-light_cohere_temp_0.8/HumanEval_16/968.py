```python
def count_distinct_characters(string):
    """ 
    Returns the number of distinct characters in the string, 
    regardless of case.
    """
    string = string.lower()  # Convert all string to lowercase to ensure all characters are distinct 
    return len(set(string))

# Test cases
'>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```
Do you like to test and use this function with different inputs?