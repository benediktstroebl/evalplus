```python
def pairs_sum_to_zero(l):
    return sum(set(l)) == 0

#Test cases
 assert(pairs_sum_to_zero([1, 3, 5, 0]) == False)
 assert(pairs_sum_to_zero([1, 3, -2, 1]) == False)
 assert(pairs_sum_to_zero([1, 2, 3, 7]) == False)
 assert(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True)
 assert(pairs_sum_to_zero([1]) == False)
```
This code defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if the list has two distinct elements that sum to zero, and `False` otherwise. The test cases cover various scenarios, including lists with no zero sum, lists with one element, and lists with a combination of elements that sum to zero.