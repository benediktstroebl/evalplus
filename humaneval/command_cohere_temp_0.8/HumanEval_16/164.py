Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters in the string, regardless of case. In the self-contained code block, it uses a set to store unique characters after lowercasing all characters in the input string. This approach ensures that both `xyzXYZ` and `Jerry` give correct outputs of 3 and 4, respectively, as specified in the problem statement.