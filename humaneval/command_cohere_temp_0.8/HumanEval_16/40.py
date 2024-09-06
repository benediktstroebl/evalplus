Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters in the provided string, regardless of case. It then returns the length of this set, indicating the number of distinct characters. The tests provided are simple and should be easily passed by this function. 

```python
# Test 1
assert count_distinct_characters('xyzXYZ') == 3

# Test 2
assert count_distinct_characters('Jerry') == 4
```
This is a simple and effective solution to the problem, but any changes to the function signature or substantial variations in the behavior of this function may result in the need for changes in the provided tests.