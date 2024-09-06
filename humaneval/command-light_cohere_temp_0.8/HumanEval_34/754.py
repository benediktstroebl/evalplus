```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -LLONG_MAX, -LLONG_MIN]]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [-10, 10, -5, 5, 0, 6],
        [123, 0, "asdf", 123, "hello"],
        [True, 1, 2, 3]
    ]
    
    for test_set in tests:
        assert unique(test_set) == test_set
```