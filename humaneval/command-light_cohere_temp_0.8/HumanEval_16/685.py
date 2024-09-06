Here's the self-contained Python function that solves the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not string.isalpha(c)})
```
This function utilizes a dictionary comprehension to create a dictionary of characters from the input string, and then checks each character against the lowercase version of all characters in the string using the `isalpha` method. It returns the the this count of distinct characters in the string, which is then returned.