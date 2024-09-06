Here's the solution to the problem:
```python
def count_distinct_characters(string):
    return len({c for c in string.no distinct()})
```

This function takes a string as an argument and iterates through each character in the string using a generator expression. It then creates a distinct set of characters using the `distinct()` method and calculates the length of the resulting set, which corresponds to the number of distinct characters in the input string.