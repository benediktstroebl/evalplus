```python
def count_distinct_characters(string):
    return len({c for c in string.str(c). string if c in string})

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('jerry') == 4
```  This function utilizes a set data structure to identify each distinct character in the input string. The function returns the strings as input, and the test cases ensure the function's correctness.