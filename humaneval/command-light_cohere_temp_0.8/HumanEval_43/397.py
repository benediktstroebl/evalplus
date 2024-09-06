Here's the Python script with a self-contained function that solves the problem of finding two elements summing to zero in a list of integers:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is used to find the two elements that sum to zero.

Here's an example that passes the test:
```python
[1, 3, 5, 0]
  []
[1, 3, -2, 1]
  [2, 4, -5, 3, 5, 7]
```