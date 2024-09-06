Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are considered the same. The number of elements in the set is then returned, which corresponds to the number of distinct characters in the string.

To verify the functionality of the function, you can use the following tests:
```python
test_1 = 'xyzXYZ'
test_2 = 'Jerry'

assert count_distinct_characters(test_1) == 3, "Should count 3 distinct characters in 'xyzXYZ'"
assert count_distinct_characters(test_2) == 4, "Should count 4 distinct characters in 'Jerry'"
```
These tests cover different scenarios and ensure that the function behaves as expected.