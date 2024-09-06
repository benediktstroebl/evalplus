```python
def count_distinct_characters(string):
    return len(set(string.isupper()))

# Tests
test_passes = [
    ("xyZS", 3),
    ("jerry", 4),
    ("JER riey", 4),
    ("XxX", 2),
    ("\u0000", 0),
    ("ABC", 3)
]

for text, expected in test_passes:
    actual = count_distinct_characters(text)
    assert actual == expected, f"Error: {text} should have {expected} distinct characters"
```