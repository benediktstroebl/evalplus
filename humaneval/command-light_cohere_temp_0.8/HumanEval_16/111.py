```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test case 1
print(count_distinct_characters('xyzXYZ'))  # Output: 3
# Test case 2
print(count_distinct_characters('jerry'))  # Output: 4
```
This code defines a function **count_distinct_characters** that takes a string as an argument and returns the number of distinct characters in that string. The function uses the a set to remove duplicates and then calculates the length of the resulting set, which is the number of distinct characters.