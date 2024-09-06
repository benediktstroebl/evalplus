Here is a Python script with a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len(set(string.lower()))
```
This script defines a function, `count_distinct_characters`, which takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses the string.lower() method to convert all string to lowercase, then uses the `set()` function and `len()` function to count the number of unique characters in the lowercase string.

The following are some sample inputs and outputs:
```python
# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))    # Output: 4
```
The function provides an efficient way to count the number of distinct characters in a given string, regardless of case.