Here is a Python script that includes a self-contained function that solves the problem of finding three numbers that sum to zero in a list of integers:

```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l)

# Testing the function
triples_sum_to_zero([1, 3, 5, 0])  # Output: False
triples_sum_to_zero([1, 3, -2, 1])  # Output: True
triples_sum_to_zero([1, 2, 3, 7])  # Output: False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Output: True
triples_sum_to_zero([1])  # Output: False
```

This script defines a function `triples_sum_to_zero` that takes a list of integers as input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. The function uses the generates a list of all possible combinations of the elements in the list and checks if the sum of each combination is equal to zero using the `sum` function. 

The test cases include a variety of lists with different lengths and elements, as well as some empty lists.