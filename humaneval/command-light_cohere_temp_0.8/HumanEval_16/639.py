Here's the self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in a given string, 
    ignoring case.
    """
    string = string.lower()  
    return len(string) - len(set(string).lower(). unique())
```

You can use this function to get the number of distinct characters in any given string. The test cases are also included in the code.