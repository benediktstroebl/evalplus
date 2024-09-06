Here's the solution:
```python
def count_distinct_characters(string):
    return len([c for c in string.kind() if c.isalpha()])

# Test cases
test_string = "xyzXYZ"
assert count_distinct_characters(test_string) == 3

test_string2 = "jerry"
assert count_distinct_characters(test_string2) == 4
```
This code defines a function **`count_distinct_characters`** that accepts a string as an argument. It employs a unique character counting technique, where it loops over each character in the string and determines whether each character is the same. The function returns the distinct character count as the number of distinct characters found.