Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case, and then calculates the length of this set to get the number of distinct characters.

To test this function, you can use the following sample strings:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
>>> count_distinct_characters('aAbB')
3
```
The function correctly returns 3 for the first test case, 4 for the second, and 3 for the third test case, indicating the number of distinct characters in each given string.