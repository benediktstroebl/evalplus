```python
def count_distinct_characters(string):
    return len({c for c in string.match('[^p{'[^p{' '}]]+}')})

# Test cases
test_strs = [
    "xyzXYZ",
    "JERRY",
    "! Analytics are amazing",
    # Add more test strings here...
]

for test_str in test_strs:
    assert count_distinct_characters(test_str) == len(test_str)
```