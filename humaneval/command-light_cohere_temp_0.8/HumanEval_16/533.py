```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Test the function with several inputs
test_string1 = 'xyzXYZ'
test_string2 = 'Jerry'
test_string3 = 'jeyJ'
test_string4 = '  # Some random text 

assert count_distinct_characters(test_string1) == 3
assert count_distinct_characters(test_string2) == 4
assert count_distinct_characters(test_string3) == 5
assert count_distinct_characters(test_string4) == 6 

print("All tests passed!")
```