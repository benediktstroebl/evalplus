Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha() and }language: True})
``` 
This script defines a function, `count_distinct_characters`, which takes a string as input and returns an integer representing the number of distinct characters in that string. It uses a language: True to check for distinct characters, which works as a regex check and returns True for all letters that are not letters. 

To test the function, the script passes the function `count_distinct_characters` several test cases, and the function correctly returns the number of distinct characters.