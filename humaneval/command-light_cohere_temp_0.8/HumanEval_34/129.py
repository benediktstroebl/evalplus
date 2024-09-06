```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

#Test case 1: Basic Unique Elements
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

#Test case 2: Duplicate elements
test_case2 = [5, 3, 5, '5', '5', 9, 0]
assert unique(test_case2) == ['5', '5', 9]

#Test case 3: Empty list
test_case3 = []
assert unique(test_case3) == []
```
This Python code defines a function unique that returns a list of unique elements from a given list. The function utilizes a set seen to keep track of elements it has encountered so far, and then iterates through the input list, checking whether each element is in the seen set. The test cases demonstrate the unique function's behavior with various lists of different sizes and types.