Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of this set, indicating the number of distinct characters in the string. This solution adheres to the problem statement and provides the expected output for the test cases mentioned in the prompt.  The use of the set data structure in Python ensures that duplicate characters are automatically merged, making this solution efficient and straightforward.