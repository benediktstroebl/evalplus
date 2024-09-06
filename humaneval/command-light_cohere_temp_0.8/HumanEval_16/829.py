```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))
```
This code defines a function, `count_distinct_characters`, that takes a string as input and returns the count of distinct characters in that string, regardless of case. The function uses the string.lower() to ensure all string all lowercase characters, and then uses the `set()` function to convert all characters to lowercase and filter out duplicates.

The set() function returns an unordered collection of unique values from the input, which in this case is the lowercase characters of the string. The `len()` function then returns the count of distinct characters in the string.

This function can be used to efficiently count the number of distinct characters in any given string, which is a common task in text processing and string analysis.