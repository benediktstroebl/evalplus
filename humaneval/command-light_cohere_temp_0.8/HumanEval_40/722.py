```python
def triples_sum_to_zero(lst):
    sum_to_zero = sum(map(sum, lst))
    return sum_to_zero == 0

#Test cases below:
1. clean a list of integers with 3 distinct elements whose sum is 0: pass
2. test a list with two equal elements, 3 greater than them, and a negative number: fail
3. test a list with one element: fail

```