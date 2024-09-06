```python
def triples_sum_to_zero(lst):
    if sum(set(sum(x) for x in lst) <= 0):
        return True
    else:
        return False

#Test the function with various inputs
test_ triples_sum_to_zero([1, 3, -2, 1], [2, 4, -5, 3, 9, 7], [1])
# Expected output: True
test_ triples_sum_to_zero([1, 2, 3, 7], [1])
# Expected output: False
test_ triples_sum_to_zero([1])
# Expected output: False
test_ triples_sum_to_zero([0])
# Expected output: False
test_ triples_sum_to_zero([1, 2, 3, 7])
# Expected output: True
```
The code defines a function triples_sum_to_zero that takes a list lst as input. It then iterates over theater list and for each iteration sums up all elements in the list and checks whether the sum is less than or equal to zero. If the sum is zero, it returns True, indicating that there are three distinct elements in the list whose sum is zero. If the sum is not zero, it returns False.