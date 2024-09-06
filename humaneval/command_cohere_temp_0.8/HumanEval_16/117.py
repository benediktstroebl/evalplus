Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of the resulting set, which is the number of distinct characters in the string. The tests correspond to the provided examples in the problem statement. 
Here is the expected output for the provided tests:
```
4
3
```