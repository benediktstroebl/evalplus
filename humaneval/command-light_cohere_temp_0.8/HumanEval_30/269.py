```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

#Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([]), [])
assertEqual(get_positive([-777, 11, 88]), [])
```  This Python function, `get_positive`, takes a list `l` as input and returns a new list containing only the positive elements from `l`. The function uses list comprehension to filter out the positive elements from the input list. 

This function is self-contained and provides a clear and concise way to solve the problem.