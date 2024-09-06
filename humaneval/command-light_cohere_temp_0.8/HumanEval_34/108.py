```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test 1
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
assert result == [0, 2, 3, 5, 9, 123]

# Test 2
test_list2 = list({3, 2, 5, unique({1, 2, 3}), 0})
result = unique(test_list2)
assert result == [2, 3, 5]

# Test 3
test_list3 = [(), (1, ), {1}]
result = unique(test_list3)
assert result == []
```