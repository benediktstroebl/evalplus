Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The function `count_distinct_characters` takes a string as an argument and counts the number of distinct characters in the string. The function uses a set to store the characters, ensuring that each character only counts once, regardless of the case. The number of keys in the set is then returned, which gives the number of distinct characters. 

Here's how the function behaves with the given inputs:
```
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```
This version of the code ensures simplicity, efficiency, and readability, making it a useful and reusable solution.