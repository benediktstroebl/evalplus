Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters, and then counts the number of distinct characters in the set. The `lower()` method is used to ensure that uppercase and lowercase variations of the same character are counted as one. 

Here is an example usage of this function:
```python
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
```
This function should return 3 for the first test case, since 'xyz' contains three different characters, and it should return 4 for the second test case, since 'Jerry' contains four different characters.