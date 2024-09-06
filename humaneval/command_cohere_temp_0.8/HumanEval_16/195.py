Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of this modified character set, which represents the number of distinct characters in the string. This solution adheres to the problem statement in the prompt, and the function is encapsulated and standalone, making it ready for use outside of any specific testing framework.