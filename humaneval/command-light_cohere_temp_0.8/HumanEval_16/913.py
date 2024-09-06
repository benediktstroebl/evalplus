```python
def count_distinct_characters(string):
    return len({c for c in string.cs.lower() if(c) for c in string})

# Test case 1: Basic string
assert count_distinct_characters('abc') == 3

# Test case 2: All uppercase letters
assert count_distinct_characters('XYZ') == 3

# Test case 3: Mixed case
assert count_distinct_characters('jerry') == 4
```  This function generates the count of distinct characters from a string, regardless of case, and does so with the 'lower()each' method. The test cases ensure that the function produces the expected results.