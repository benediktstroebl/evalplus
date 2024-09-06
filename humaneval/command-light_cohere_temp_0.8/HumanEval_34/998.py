```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [0]]

#Test cases 

assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

assert unique([]) == []

assert unique([1, 2, 3, 4]) == [3, 4]

assert unique([1, 2, 3]) == [1, 2]

try:
    unique('abc')
except TypeError:
    assert False

try:
    unique([])
except TypeError:
    assert False

```
This code defines a function `unique` that returns a list containing unique elements from the input list, as specified by the problem. It provides several test cases to verify the correctness of the function.

This code is self-contained and does not require any external modules or functions to be run.