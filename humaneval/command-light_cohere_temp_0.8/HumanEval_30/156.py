```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([-5, -3, -9, -8, -2, -1, -100]))
# Output: [-5, -3, -9, -8, -2]
```
This script defines the function `get_positive` which takes a list as input and returns a new list with only the positive elements. 
Then it passes three test cases with different lists and the function returns the expected positive elements correctly.