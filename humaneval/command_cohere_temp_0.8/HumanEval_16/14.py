Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case, and then returns the set's length to provide the number of distinct characters.

To apply this function to test cases, you can call it with different input strings, as demonstrated in the provided test cases:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```
The function passes both test cases correctly as it returns 3 for the first string and 4 for the second string, which aligns with the problem's expectation of counting distinct characters regardless of case.  This solution is efficient with a time complexity of O(1) due to the use of the set data structure.