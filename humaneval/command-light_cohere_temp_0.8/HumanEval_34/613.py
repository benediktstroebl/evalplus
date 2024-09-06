```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    unique = set(l)
    return list(unique)

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))  # expected output: [0, 2, 3, 5, 9, 123]

#Test case 2
test_case2 = [10, 11, 12, 13, 7, 8, 9]
print(unique(test_case2))  # expected output: set([10, 11, 12, 13, 7, 8])

#Test case 3
test_case3 = "abc"123"
print(unique(test_case3))  # expected output: []
```