Here's a self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    string = ''.join(). lower(string, str. .alphanumeric=str.
    return len(set(string))
```
This function takes a string as input and uses the `str.lower()` method to convert it to lowercase. Then, the `str` module's `isalphanumeric` filter is used to remove all non-alphanumeric characters from the string.