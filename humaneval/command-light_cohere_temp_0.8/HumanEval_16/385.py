```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters()})
count_distinct_characters('xyzXYZ')
 # Answer: 3
count_distinct_characters('JER')
 # Answer: 4
```
This code defines a function called `count_distinct_characters` that takes a string as an argument and returns the number of distinct characters in that string. It uses a simple set of characters and iterates through them to check if each one is distinct, which is the same as checking if it's not in the string already.