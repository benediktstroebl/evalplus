Here's a Python script with a self-contained function that solves the problem of checking whether any two elements in a list sum to zero:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension checks if each element in the list sums to zero.
    If elements that sum of two are distinct elements are equal to zero, it returns True, otherwise False.

```
Here are some test cases to verify the correctness of the function:
```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))          # Output: False
```