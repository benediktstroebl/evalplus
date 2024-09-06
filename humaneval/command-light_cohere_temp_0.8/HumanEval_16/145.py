Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper(c)})
```

This function uses a list comprehension to create a new set of characters that are the uppercase versions of each character in the original string. 
The set comprehension ensures that only unique characters are counted, regardless of their case. 

The function then returns the length of this new set, which is the number of distinct characters in the original string.