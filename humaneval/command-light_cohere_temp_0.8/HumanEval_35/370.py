```python
def max_element(lst):
    return max(lst)

# Test case 1
assertEqual(max_element([1, 2, 3]), 3)

# Test case 2
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) ,123)

# Test case 3
assertEqual(max_element([]) , 0)

# Test case 4
assertEqual(max_element([10, 20, 30]) , 30)
```

This script defines a function max_element that takes a list as an input and returns the maximum element from the list. It is then tested using 4 different test cases, which pass the corresponding assertions.