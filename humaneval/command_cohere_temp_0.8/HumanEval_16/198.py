Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, ignoring case, and then returns the set's length to provide the number of distinct characters.

To demonstrate its usage, you can add a test case in the same script or simply test it with various input strings. Here's an example:
```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This will output:
```
3
4
```
 Showing that the function accurately counts the distinct characters based on the given problem statement.  If you need further assistance or have more questions related to this problem, feel free to ask!