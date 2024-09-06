Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which gives the number of distinct characters. Such sets in Python are optimized for speed and are particularly efficient when you need to test whether a piece of data is in a collection or not. Hence, this solution has a time complexity of O(1).