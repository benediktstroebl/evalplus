Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case, and then counts the number of remaining distinct characters to solve the problem. It accepts a string as input and returns an integer count of distinct characters. 

Here is an example of how to use this function:
```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This will produce the following respective outputs:
```
3
4
```