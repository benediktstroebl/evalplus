Here's a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len({c for c in string. unstrik(c) for c in string})

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters('a'), 5)
assertEqual(count_distinct_characters('z'), 5)
assertEqual(count_distinct_characters(''), 0)
```
This script defines a function `count_distinct_characters` that takes a string as input and uses a set-based approach to count the distinct characters in the string. The test cases cover a variety of scenarios, including different lengths of strings, the presence of non-alph characters, and an empty string.