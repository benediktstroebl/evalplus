Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which gives the number of distinct characters. The function ignores the case, counting 'x', 'X', and 'xX' as just one character. The tests correspond to the ones provided as prompts so should be good to go!