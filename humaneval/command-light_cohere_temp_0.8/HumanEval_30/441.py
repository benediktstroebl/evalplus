```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test case 1
print("Test case 1 result:", get_positive([-1, 2, -4, 5, 6]))
[['2', '5', '6']]

#Test case 2
print("Test case 2 result:", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
 [['5', '3', '2', '3', '9', '123', '1']]

#Test case 3
print("Test case 3 result:", get_positive([5, 3, -5, 2, -3, 3, 9, 0, -4, 7, 8]))
 [['5', '3', '2', '3', '9', '7', '-4', '8']]
```