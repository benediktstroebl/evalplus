Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase and then uses the `set` data structure to automatically filter out duplicate characters. 

The set abstraction in Python employs the Merkle Tree data structure which uses a hash function to determine whether new items are duplicates or not. Hence, the set effectively holds unique characters while having a linear time complexity of O(n) for insertion and deletion. This makes it a very efficient and handy tool for the purpose.

The function then returns the length of the character set, indicating the number of distinct characters in the input string.