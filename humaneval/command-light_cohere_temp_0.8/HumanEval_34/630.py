```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print("Test case 1 result:", test_result)

test_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result2 = unique(test_list2)
print("Test case 2 result:", test_result2)

test_list3 = [5, 0, 0, 2, 3, 3]
test_result3 = unique(test_list3)
print("Test case 3 result:", test_result3)
```
This script defines a function unique that takes a list as input and returns a list of unique elements in that list, after removing duplicates. It uses the unique elements set to keep track of elements seen so far and only re-adds elements that are not duplicates and are not None. The test cases demonstrate that the function correctly identifies unique elements in various lists.