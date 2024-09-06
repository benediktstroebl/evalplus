```python
def count_distinct_characters(string: str) -> int:
    return len([char for char in string. distinct()])

# Simple test case
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))  # Output: 4)

# Another test case with more characters
print(count_distinct_characters('abcABCdef'))  # Output: 5)
```  This code defines a function **`count_distinct_characters`** that accepts a string as an argument. It uses the unique method to create a list of unique characters in the string. This list contains only letters (both lowercase and uppercase), so the length of this list is the number of distinct characters in the string.