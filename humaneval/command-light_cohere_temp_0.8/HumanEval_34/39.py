```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x += 1)
    return result

# Tests
def test_unique():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(test_list) == [0, 2, 3, 5, 9, 123]
test_list2 = [4, 7, 2, 9, 6, 6, 99]
    assert unique(test_list2) == [2, 9]
```