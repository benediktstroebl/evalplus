Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. Finally, it returns the length of the set, which is the number of distinct characters. 

Here's the markdown code block as you requested:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
You can copy and paste this code block into a Python environment or script to use the `count_distinct_characters` function.