Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase to ensure that characters are treated as the same regardless of case and then calculates the number of distinct characters by returning the length of the set. 

Here is an example of how to use this function:
```python
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
```
This function achieves the same behavior as the specified problem statement.