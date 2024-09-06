```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == 0]

# Test cases
tests = {
    "Test basic operation":
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    , "Test empty list": []
    , "Test list with duplicates": [5, 3, 5, 2, 3, 3]
    , "Test large list": [x for x in range(1000)]
    }

# Run the tests
for item in tests. unique unique(item)
```