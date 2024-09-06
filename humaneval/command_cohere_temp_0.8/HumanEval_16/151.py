Here's a Python script that contains a function to solve the problem you've described:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case, ensuring that each character is counted only once. It then returns the count of unique characters in the set. The overall time complexity of this solution is O(M), where M represents the size of the input string.