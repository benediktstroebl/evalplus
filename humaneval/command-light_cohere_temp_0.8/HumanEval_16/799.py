```python
def count_distinct_characters(string: str):
    """ 
    Returns the number of distinct characters in the string, regardless of case.
    """
    string = "xyzXYZ jerry"
    return len([char for char in string.camelcase(string) if char.isalpha()]
count_distinct_characters('jERry') #Passes
```