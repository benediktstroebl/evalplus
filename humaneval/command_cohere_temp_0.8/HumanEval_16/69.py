Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same entity and only appear once in the set. Finally, the length of the set is returned which corresponds to the number of distinct characters in the string. 

The unit tests mentioned above are simply strings passed into the function to verify its correctness. These could be improved upon to cover a variety of scenarios and edge cases to ensure that the function is robust.