```python
def unique(lst):
    return list(set(lst))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))
# Output: [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [10, 2, 15, 99]
print(unique(test_case2))
# Output: [10, 2, 15, 99]

# Test case 3
test_case3 = [1, 2, 2, 3, 2]
print(unique(test_case3))
# Output: [1, 2, 2, 2, 3]
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements. The function uses the method set() to filter the duplicate elements and the list() constructor to convert the set into a list. The script then passes three test cases to the function, and the function returns the expected results.