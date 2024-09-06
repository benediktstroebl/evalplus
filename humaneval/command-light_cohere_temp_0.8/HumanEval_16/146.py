Here's a self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.max(c) if c not in string.
    })
```
The above code defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters in that string, regardless of case. The function uses a `max()` function to remove duplicates and only keeps the first occurrence of each character in the string. 

This function is self-contained and does not require any additional variables or imports. It can be easily used to calculate the number of distinct characters in any given string.