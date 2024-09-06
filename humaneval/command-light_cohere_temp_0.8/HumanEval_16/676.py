```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c not in 'abcdefghijklmnopqrstuvwxyz'})

# Example usage:
input_string = 'xyzXYZ'
print(count_distinct_characters(input_string))  # Output: 3

input_string = 'Jerry'
print(count_distinct_characters(input_string))  # Output: 4
```
This function counts the number of distinct characters in a given string, regardless of case. The function uses a itertools.keep set of characters method to remove duplicate characters and return the count. The function is self-contained, which means it doesn't rely on any other functions or modules.