```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
   
    checks if there are two elements in the list whose sum equals zero,
    returns True, and removes these two elements from the list.

# Example usage:
test_cases = [1, 3, 5, 0, -2, 1]
if pairs_sum_to_zero(test_cases):
    print("pass")
else:
    print("fail")
```
The code defines a function called pairs_sum_to_zero that takes a list of integers as an input parameter. It returns "True" if there exist two distinct elements in the list whose sum equals zero, and it returns "False" Otherwise.