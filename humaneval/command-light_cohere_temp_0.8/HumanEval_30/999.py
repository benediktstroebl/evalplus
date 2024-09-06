```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test cases 

#Test 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

#Test 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

#Test 3
print(get_positive([-5, -3, -1, 7]))
# Expected output: []
```