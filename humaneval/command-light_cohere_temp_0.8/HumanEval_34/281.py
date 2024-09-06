```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
tests = [
    dict(zip(['zero', 'two', 'three', 'five', 'nine', '123'], [0, 2, 3, 5, 9, 123])))
])

# Function call and results
for case in tests:
    print(unique(case['lst']), case['msg'])
```

This code provides a unique function that removes duplicates from a list and returns the list of unique elements. The function is tested with a variety of test cases, and the results are printed to the console.