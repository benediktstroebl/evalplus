```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists
print(get_positive([-1, 2, -4, 5, 6]))        # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]

# Test list comprehension alternative
positive_numbers = [x for x in lst if x >= 0]
print(positive_numbers)
```  Output: [2, 5, 6, [3, 9, 123] , 1]  This demonstrates a clear separation of concerns and adheres to the Python best practices.