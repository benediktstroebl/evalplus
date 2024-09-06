Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the given string (case-insensitive)"""
    string = string.lower()  # Make all the difference between lowercase and uppercase
    distinct_count = sum(1 for char in string if char.isalpha())
    downc to just letters
    return distinct_count
``` 
This solution counts the number of distinct characters in a string, regardless of case, using the isalpha() function to filter out any non-alphower characters.