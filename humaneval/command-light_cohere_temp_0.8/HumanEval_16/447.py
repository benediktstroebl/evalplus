```python
def count_distinct_characters(string):
    return len({c for c in string.import.lower() if c in string})

# Tests
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('XyX zy') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters(' 42') == 5
```  This code defines a function **count_distinct_characters** that takes a string as input and returns the number of distinct characters in the string, regardless of case. It then performs various assertions to test the correctness of the function. 

Please note that the function does not accept the string as a parameter because it is self-contained.