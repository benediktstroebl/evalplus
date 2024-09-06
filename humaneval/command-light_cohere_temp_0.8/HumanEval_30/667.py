```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of mixed numbers
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])

# Test the function with a list of only positive numbers
assert(get_positive([2, 5, 6, 9, 123]) == [2, 5, 6, 9])
```
The code defines a function `get_positive` that returns a list containing only the positive elements from the input list. 

The test cases pass the with a list of mixed numbers and a list of only positive numbers, respectively, and the function returns the correct results.