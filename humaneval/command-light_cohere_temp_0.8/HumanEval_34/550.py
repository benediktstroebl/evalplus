```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
 return list(result)
    return result

# Test cases
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]
test_unique = unique([6, 6, 2, 1, 5])
assert test_unique == [2, 1, 5]
test_unique = unique([])
assert test_unique == []
test_unique = unique([1, 2, 2, 2])
assert test_unique == [2, 2]
```

This function unique will help you manage lists of items and ensure that only unique items are retained, which is useful for various applications of data processing.