```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [float('inf'), 5, 3, 2, 3, 3, 9, 0]
assert unique(test_case2) == [5, 3, 2, 3, 9]

# Test case 3
test_case3 = ['a', 'apple', 'b', 'apples', 'x']
assert unique(test_case3) == ['a', 'apple', 'b', 'apples']
```
The function unique is designed to return a list containing only the unique elements from the input list. This is an approach that utilizes a set to keep track of seen elements and then filters out duplicates to provide the desired output.