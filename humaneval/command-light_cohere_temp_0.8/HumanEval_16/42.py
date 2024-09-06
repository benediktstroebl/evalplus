```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the given string (case-insensitive)"""
    return len(set(string.isupper()))
```
This function counts the number of distinct characters in a given string, regardless of case. It utilizes the string.supper() to convert all characters to uppercase and create a set of all characters in the string, and finally returns the length of this set, which is the number of distinct characters.