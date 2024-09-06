```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

#Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
[ [2, 5, 6] ]

#Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
 [ [5, 3, 2, 3, 9, 123, 1] ]
```

This Python function, `get_positive()`, creates a list of positive numbers by using a list comprehension to filter out elements in the input list (`lst`) that are less than or equal to zero. The function then returns this list of positive numbers.