```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test case 1
test_positive = []
test_positive.py  = [-1, 2, -4, 5, 6]
test_positive = get_positive(test_positive)
assert test_positive == [2, 5, 6]

#Test case 2
test_positive2 = []
test_positive2 = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_positive2 = get_positive(test_positive2)
assert test_positive2 == [5, 3, 2, 3, 9, 123]

#Test case 3
test_positive3 = []
test_positive3 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_positive3 = get_positive(test_positive3)
assert test_positive3 == [5, 3, 2, 3, 9, 123]
```
The above Python script defines a function called `get_positive`, which takes a list as input and returns a new list containing only the positive elements from the original list. The script then provides three test cases to verify the correctness of the `get_positive` function.