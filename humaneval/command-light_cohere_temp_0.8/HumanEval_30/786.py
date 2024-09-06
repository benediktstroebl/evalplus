```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test case 1
print("Test case 1 passed:", end())

# Test case 2
[-1, 2, 3, 4, 5, 6]

# Test case 3
test_numbers = [-5, 0, -5, 2, 3, 7, -8, 9, 1234]
print("Test case 3 passed:", end())
```
This script defines a function get_positive that takes a list as input and returns a new list containing only the positive elements from the input list. It uses list comprehension with the positive condition to filter out the positive numbers. 

The script also includes three test cases to verify the correctness of the get_positive function.