Here's a Python script that contains a function called `count_distinct_characters` which takes a string as an argument and returns the number of distinct characters (regardless of case) in the string:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The function uses a set to remove duplicate characters and to disregard the case, and then proceeds to count the number of remaining characters which correspond to the number of distinct characters. You can use it by calling the function with a string argument like this:
```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
``` 

This should output `3` in both cases, as those are the number of distinct characters.