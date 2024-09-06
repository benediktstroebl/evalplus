```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
test_count_distinct_characters = lambda: [count_distinct_characters('xyzXYZ') == 3] and \
                                           [count_distinct_characters('jerry') == 4]

if test_count_distinct_characters():
    print('The function works! Passes all tests.')
else:
    print('The function does not work.')
```