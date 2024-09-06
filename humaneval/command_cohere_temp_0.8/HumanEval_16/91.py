Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which corresponds to the number of distinct characters. 

Here's the markdown code block containing the function as required:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```