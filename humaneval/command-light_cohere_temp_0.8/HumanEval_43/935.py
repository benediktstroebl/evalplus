```python
def pairs_sum_to_zero(l):
    return sum(x + y for x, y in zip(l, l[1:])) == 0

# Test the function with various inputs
 assert pairs_sum_to_zero([1, 3, 5, 0]) == False
 assert pairs_sum_to_zero([1, 3, -2, 1]) == False
 assert pairs_sum_to_zero([1, 2, 3, 7]) == False
 assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
 assert pairs_sum_to_zero([1]) == False
 ```