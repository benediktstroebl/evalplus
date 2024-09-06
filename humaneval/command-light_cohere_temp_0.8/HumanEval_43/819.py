```python
def pairs_sum_to_zero(lst):
    sum_to_zero = False
    for x, y in zip(lst, lst[1:]):
        if x + y == 0:
            sum_to_zero = True
            break
    return sum_to_zero

# Test the function
test_sum_to_zero = pairs_sum_to_zero([1, 3, -2, 1], [1, 2, 3, 7])
print(test_sum_to_zero)
```
We are using two lists, [1, 3, -2, 1] and [1, 2, 3, 7], with the test_sum_to_zero function to determine if the two lists have two distinct elements whose sum is zero. The output of the test_sum_to_zero will be True since the lists have the property where every element's sum equals zero.