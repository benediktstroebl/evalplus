```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Unit tests
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]
test_empty = []
assert unique(test_empty) == []
test_single = [1]
assert unique(test_single) == [1]
```
The function unique takes a list as an argument and returns a new list containing only the unique elements from the input list. The function uses a set to keep track of the elements that have been encountered so far. The loop iterates through the unique elements from the input list, and adds them to the result list if they are not already present in the seen set. The function returns the value of the resulting unique list.