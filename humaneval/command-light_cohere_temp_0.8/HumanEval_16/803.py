Here is a Python script with a self-contained function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters (regardless of case) in that string. The function uses the string.lower() method to convert all input string into lowercase characters, then uses the `set` function to create a set of all lowercase characters in the string. The `len` function then counts the number of distinct characters in the set, which is also the same as the number of unique characters in the original string.