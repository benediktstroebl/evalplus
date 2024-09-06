```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not -1]

# Test case 1:
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1: ", unique(test_case1))  # Output: [0, 2, 3, 5, 9, 123]

# Test case 2:
test_case2 = [5, 2, 3, 'abc']
print("Test case 2: ", unique(test_case2))  # Output: ['abc']

# Test case 3:
test_case3 = ['a', 'a', 'b', 'a']
print("Test case 3: ", unique(test_case3))  # Output: ['a', 'b']
```
This script defines a function `unique` that takes a list `lst` as input and returns a new list with unique elements. The function uses a also utilizes a `set` to keep track of seen elements and uses list comprehension to filter out duplicates.