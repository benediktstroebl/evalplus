```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))

# Test case 2
test_case2 = [5, 3, 'abc', 5, '123', 'abc-123', 0]
print(unique(test_case2))

# Test case 3
test_case3 = [b'abc', b'b', a', b)
print(unique(test_case3))
```
The provided Python script defines a function `unique` that takes a list `lst` as an argument and returns a new list with the unique elements from the original. The function utilizes a set to keep track of the seen elements, then iterates through the list and adds elements to the set. It returns the unique elements from the set of elements.