```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    return len([c for c in string.lower() if c not in string.lower()])
return
``` 
This code defines a function called `count_distinct_characters`, which takes a string as input and returns the count of distinct characters in the string, regardless of case. The function achieves this by utilizing a list comprehension with a `not in`.the. As well as the saw in the function that makes it self-contained.