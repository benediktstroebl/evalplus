Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, ignoring case, and then returns the set's length.

To demonstrate its behavior, here's a quick example:
```python
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
```
This approach ensures fast and efficient distinct character counting, regardless of the string's length or content.