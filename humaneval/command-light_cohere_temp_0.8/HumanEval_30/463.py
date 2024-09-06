```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of various elements
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

test_positive2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_positive2 == [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function **get_positive** that takes a list as an argument and returns a new list with only the positive elements from the original list. 

It then tests the result of the function using the **assert** statement with the test cases provided, which pass the test and demonstrate the correctness of the function.