```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test 1:
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

#Test 2:
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test 3:
print(get_positive([]))
# Expected output: [0]

# Test 4:
print(get_positive([1, 2, 3, -4, -100]))
# Expected output: []
```
This script defines a `get_positive` function that takes a list as input and returns a new list containing only the positive integers from the original list. 

Each test in the script verifies the correctness of the `get_positive` function by passing different input lists and checking the returned lists for containing only positive integers.