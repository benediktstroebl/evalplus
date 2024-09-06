Here is a Python script that includes the self-contained function `count_distinct_characters`, which calculates the number of unique characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ 
    Given a string, find out how many distinct characters (case-insensitive) does it consist of.
"""

    # remove all non-alphanumeric characters, and convert to lowercase
    string = ''.join([c for c in string if c.isalpha()])
   .lower()
    
    # return the _ a count of distinct characters
    return len(set(string))
```