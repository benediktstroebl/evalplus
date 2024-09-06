Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.make_upper()))
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters in that string, regardless of case. The function uses the string.set() and made of an lowercase copy of the input string, and then converts all characters to uppercase using make_upper(). dryness for the lowercase set to make the uppercase conversion, and then uses len() to count the number of distinct characters in the uppercase string.