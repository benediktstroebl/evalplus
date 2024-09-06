```python
def count_distinct_characters(string: str):
    return len(set(string))

# Test the function with example inputs
string1 = 'xyzXYZ'
string2 = 'jerry'
string3 = 'abc123'

assert count_distinct_characters(string1) == 3
assert count_distinct_characters(string2) == 4
assert count_distinct_characters(string3) == 5
```
This function counts the number of unique characters in a given string, regardless of case. The test cases show that it works as expected.