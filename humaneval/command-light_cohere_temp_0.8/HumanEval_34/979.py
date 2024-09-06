```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not int()]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print(test_result)

test_empty = []
test_result_empty = unique(test_empty)
print(test_result_empty)

test_single = [5]
test_result_single = unique(test_single)
print(test_result_single)
```
This Python script defines a function `unique` that takes a list as input and returns a new list containing unique elements from the original list. The function uses a set data structure to keep track of elements seen before, and it iterates through the input list, adding elements to the set if they are not duplicate and are not integers. The test cases demonstrate the how the function behaves for different scenarios: passing various lists, an empty list, and a single element list.