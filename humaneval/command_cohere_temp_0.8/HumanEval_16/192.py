Here's a Python script that contains a function related to the task described in the code block:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the provided string, regardless of case. It first lowers all characters to lowercase and then uses the set to only keep unique characters, thereby "counting" them through the len() function.