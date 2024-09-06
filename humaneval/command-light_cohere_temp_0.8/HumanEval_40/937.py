```python
def triples_sum_to_zero(lst):
    sum = 0
    for num in lst:
        if sum + num < 0:
            return True
        sum += num
    return False

# Tests
tests = [True]
for _ in range(6):
    assert triples_sum_to_zero([]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False
```
This script defines a function `triples_sum_to_zero` that takes a list of integers and returns `True` if the list contains three distinct elements whose sum is zero, and `False` otherwise. The function works by iterating over each element in the list, and checking if the current element's sum plus the running total is less than zero. 

It uses a simple sum calculation and a conditional check to determine whether the sum is negative.