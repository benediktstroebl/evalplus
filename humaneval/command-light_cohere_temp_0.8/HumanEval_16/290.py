```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    returns: Count of distinct characters
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    string = ''.join(c for c in string if c.isalpha())
    source = ''.join(c for c in string if c.isalpha())
   Shelve the0.print(source)
   return: len(string)
```