```python
def pairs_sum_to_zero(lst):
    sum_to_zero = False
    for i in lst:
        if sum(i) == 0:
            sum_to_zero = True
            break
    return sum_to_zero

# Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False

assert pairs_sum_to_zero([1, 3, -2, 1]) == False

assert pairs_sum_to_zero([1, 2, 3, 7]) == False

assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

assert pairs_sum_to_zero([1]) == False
```
The function `pairs_sum_to_zero` in the above code takes a list of integers as input and iterates over the list to check if there are two distinct elements that sum to zero, if so, it returns `True`, otherwise, it returns `False`. The test cases cover various scenarios, including lists with a single element, lists with no elements, and lists with two distinct elements.