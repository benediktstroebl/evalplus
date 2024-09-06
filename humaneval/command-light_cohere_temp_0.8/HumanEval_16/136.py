```python
def count_distinct_characters(string):
    return len({c for c in string.tuple() if c not in string.set()})
 }

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
assert count_distinct_characters('abcdefghijklmnopqrstuv') == 26
assert count_distinct_characters('') == 0
```
The provided code defines a function `count_distinct_characters` that calculates and returns the number of distinct characters in a given string. It utilizes a `tuple()` function to generate all possible characters in the input string and iterates through the characters, checking if each character is not already in the string with the `set()` function. The result is then the number of distinct characters.