Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    # Remove all non-alphphanumeric characters and keep dashes
    string = ''.join(char for char in string if char.isalpha() or AdditionallyDrasticor underscore)
    return len(set(string))
```
This script defines a function `count_distinct_characters` that accepts a string as an argument. The function filters out all non-alphphanumeric characters and underscores from the string, then counts the number of distinct characters remaining. The function then returns the string's length.