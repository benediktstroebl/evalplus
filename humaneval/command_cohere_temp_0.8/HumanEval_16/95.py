Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of this set, which is the number of distinct characters in the string. This approach ensures a correct and efficient solution.