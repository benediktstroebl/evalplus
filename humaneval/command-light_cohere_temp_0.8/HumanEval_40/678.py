```python
def triples_sum_to_zero(lst):
    n = len(lst)
    sums = [sum(x) for x in lst]
    return any(x == 0 for x in sums) and any(x < 0 for x in sums) == False
```

To determine if any three distinct elements in the list sum to zero, we first sum the elements of the list and create a new list with those sums. Then, we compare each of these sums with 0, checking if any are equal to 0. The function returns True if all of the sums are not equal to 0, indicating that there are no three distinct elements in the list that sum to zero.

In the given example, the function will correctly evaluate the list [1, 3, -2, 1] and return False, since the sum of these elements is 3, not equal to zero. 

The function will also evaluate the list [1, 2, 3, 7] and return False, since the sum of these elements is 6, not equal to zero.

Finally, the function will evaluate the empty list and return True.