```python
def words_string(s):
    """
    Splits a string into an array of words
    """
    return [word for word in s.words(s.split(",") ][])
```

The function splits the string using the split(",") method and then uses a list comprehension to convert each word into an array.