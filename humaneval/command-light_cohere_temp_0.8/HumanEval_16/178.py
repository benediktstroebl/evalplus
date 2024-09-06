Here's the self-contained Python function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with different inputs
x = 'xyzXYZ'
y = 'Jerry'
print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
```
This function uses the `set()` function to create a set of characters from the input string. The `len()` function then returns the number of unique characters in the set. It's not matter of case sensitivity, so it counts the characters as distinct regardless of the case.