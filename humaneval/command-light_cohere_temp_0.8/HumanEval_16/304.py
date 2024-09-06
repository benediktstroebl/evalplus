```python
def count_distinct_characters(string: str) -> int:
    characters = set(string)
    return len(characters)

# Test the function with different inputs
assertEqual(count_distinct_characters('abc'), 3)
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('ABC'), 3)
assertEqual(count_distinct_characters('JERRY'), 4)
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. It uses the set() to collect all characters in the string into a set, and then uses the length of the set as the result. 

The test code ensures that the function works correctly for different inputs.