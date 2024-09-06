```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
    if c not in string.
    for x in string):
        if c != string[x] and c.
    }
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. 
The function uses the set difference method to iterate over each character in the string and keep track of characters that have been encountered so far. The function returns the unique character count after the process.