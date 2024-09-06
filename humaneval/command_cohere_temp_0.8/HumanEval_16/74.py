Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters in the provided string, regardless of case. It then returns the length of this set, indicating the number of distinct characters. The tests provided in the problem statement will verify this function's behavior:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
``` 
This approach works efficiently and provides the required solution for the given problem.