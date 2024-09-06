```python
def pairs_sum_to_zero(lst):
    s, = sum(lst)
    return (s < 0) and (len(lst) > 1)

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
print(test_result)

test_result = pairs_sum_to_zero([1, 3, -2, 1])
print(test_result)

test_result = pairs_sum_to_zero([1, 2, 3, 7])
print(test_result)

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
print(test_result)
```
The provided Python code defines a function named `pairs_sum_to_zero` that takes a list `lst` as input. This function aims to determine whether there are two distinct elements in the list that sum up to zero. It then returns `True` if this condition is met and `False` otherwise. The function is then tested using several sample lists and the results are printed to the console.