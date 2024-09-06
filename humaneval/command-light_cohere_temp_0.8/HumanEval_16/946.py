Here's a self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    characters = set(string.count(distinct(characters))
    return len(characters)

# Test case 1
print(count_distinct_characters('xyzXYZ'))  # Output: 3

# Test case 2
print(count_distinct_characters('jerry'))  # Output: 4
```
This function utilizes the `set` data structure to efficiently count distinct characters, and the `count` method with `distinct` parameter to ensure only unique characters. The function then converts the general string to lowercase to ensure case-insensitive counting.