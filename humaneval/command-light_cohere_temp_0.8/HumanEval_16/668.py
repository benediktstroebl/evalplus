```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))

# Example usage:
input_str = 'xyzXYZ jerryYX'
result = count_distinct_characters(input_str)
print(f"Number of distinct characters: {result}")
```
This function counts the number of distinct characters in a given string, regardless of case. Using the `set()` method with `lower()` function in Python, the function will return the number of unique characters in the string. This ensures that all characters, regardless of case, are considered distinct.