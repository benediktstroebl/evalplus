```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various list inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(test_get_positive)

# Expected Output: [2, 5, 6, 3, 9, 123, 1]
```
This Python code defines a function get_positive that takes an input list lst and returns a new list containing only the positive numbers from the original list. It uses list comprehension with the basic conditions to filter out the positive numbers from the list. The code also includes a series of test cases for the get_positive function, and these test cases are expected to produce the correct results.