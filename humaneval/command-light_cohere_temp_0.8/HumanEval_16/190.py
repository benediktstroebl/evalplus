Here is a Python script with a self-contained function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha() and!)
```

This function uses the `isalpha()` method to check if each character in the string is an alphabetic which returns `True` if the character is an alphabetic string character. 

It then uses a list comprehension to create a new list of characters that are only the distinct characters in the original string, and uses the `len()` function to get the length of this list.