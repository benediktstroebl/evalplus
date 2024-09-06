Here's the solution:
```Python
def pairs_sum_to_zero(lst):
    return sum([x for x in lst if x != 0]) == 0
```

This function aims to check whether all elements in the provided list are zero, indicating that the list can be divided by its sum without a remainder. It employs a simple set of conditions to achieve this.

The function is then tested with various input lists, and the output is evaluated against the expected results from the test cases.