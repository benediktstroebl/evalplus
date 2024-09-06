```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases with different list inputs
# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
get_positive([5, 3, -5, -6, -1, -9])
# Expected output: [5, 3, -5, -6, -1]

# Test case 4
get_positive([10, 20, 30, 40, 50, 60])
# Expected output: [10, 20, 30, 40]

# Test case 5
get_positive([1, 2, -3, -100])
# Expected output: []

# Test case 6
get_positive([1, 2, 3, -4, -5])
# Expected output: [1, 2, 3]
```
This script defines a function called **get_positive** which takes a list as input and returns a new list with only the positive elements from the original list. The function uses a iterate through list and checks if each element is greater than or equal to zero. The code also includes several test cases to validate the correctness of the function with different lists.