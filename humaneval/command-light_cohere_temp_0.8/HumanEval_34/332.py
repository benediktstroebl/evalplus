```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # [0, 2, 3, 5, 9, 123]
test_list2 = [5, 3, 5, 2, 3, 3, "test"]
print(unique(test_list2))  # ['test']
test_list3 = [5, 3, 2, 99]
print(unique(test_list3))  # []
```
This function `unique` uses the `set` method to get unique elements in a list and then returns the resulting list.