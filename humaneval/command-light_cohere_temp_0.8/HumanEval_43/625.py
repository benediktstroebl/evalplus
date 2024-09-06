```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def sum_diff_zero(a, b):
        return (a + b) - (a - b) 
	return sum_diff_zero(l[0], l[-1])
	return sum_diff_zero(l[0], l[-1])  # this should be zero
```
The function uses the built-in Python function 'sum' to calculate the sum of the list's elements and the '-' operator to calculate the difference between the two elements.