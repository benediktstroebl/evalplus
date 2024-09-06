Here is a self-contained Python script that solves the problem of getting unique elements in a list:
```python
def unique(lst):
    return list(set(lst))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
print("Test case 1 result:", result1)

# Test case 2
test_case2 = [5, 3, "abc", 5, 0, "def"]
result2 = unique(test_case2)
print("Test case 2 result:", result2)

# Test case 3
test_case3 = [1, 2, 3, 4, 5, 6, 7, 8]
result3 = unique(test_case3)
print("Test case 3 result:", result3)
```
This script defines a function `unique` which takes a list `lst` as input and returns a new list containing only the unique elements from the input list using the `set()` and `list()` functions. The `unique` function is then passed three test cases, and the results are printed.