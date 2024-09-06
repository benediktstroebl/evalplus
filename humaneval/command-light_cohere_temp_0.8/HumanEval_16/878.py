```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha()})
 unique characters in a string
``` 
This code defines a function that calculates the number of distinct characters in a given string, regardless of case. It utilizes a `is set()` function to create a set of characters in the string and checks each character against the `isalpha()` condition to ensure uniqueness. The code then counts the unique characters and returns the count as the number of distinct characters.