```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function
test_positive = get_positive([-1, 2, -4, 5, 6])
print(test_positive)
[ rushed comment about actual output intended to be shown ]

# Another test
test_positive2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(test_positive2)
``` 
This Python code defines a function named get_positive that takes a list l as input and returns a new list containing only the positive integers from the original list. The function employs a list comprehension to filter out the positive elements. It is a initial test of the function using a sample list, which should pass successfully.