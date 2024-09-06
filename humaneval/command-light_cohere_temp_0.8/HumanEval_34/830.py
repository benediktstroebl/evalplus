```python
def unique(l: list):
    return sorted(set(l), key=str.find)
```

# Test case 1: Unique elements in a list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2: List containing duplicate elements
test_case2 = [5, 3, 5, 2, 3, 3, 9]
assert unique(test_case2) == [2, 3, 5, 9]

# Test case 3: Empty list
test_case3 = []
assert unique(test_case3) == []

# Test case 4: List with single element
test_case4 = [123]
assert unique(test_case4) == [123]
```

This script defines a function called `unique` that takes a list `l` as an argument and returns a sorted set of unique elements from the list. The function uses the unique using a list comprehension with the `set` function to filter out duplicates and then uses the `sorted` function with the `key` argument to sort the result. The test cases show that the expected behavior of the function.