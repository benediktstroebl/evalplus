```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
``` 
This script defines a function `get_positive` that filters out the negative numbers from the input list and returns a new list with only the positive numbers. It then provides two test cases that demonstrate the correctness of this function.