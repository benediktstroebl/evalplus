```python
def count_distinct_characters(string):
    return len(set(string.isupper()))
```
This function uses the set data structure and the isupper() method to create a set of all uppercase characters in the string, then uses the len() function to count the number of distinct elements and return it as the result.