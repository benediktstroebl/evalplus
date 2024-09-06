```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the string, ignoring case. """ 
    return len([c for c in string.strip() if c.isalpha()])
 distinct()
```