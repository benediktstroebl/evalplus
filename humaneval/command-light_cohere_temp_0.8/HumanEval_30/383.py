```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```