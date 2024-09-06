```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the entire file and test your solution with the tests.
    return len(set(zip(lst, lst[1:], lst[2:] + [0]))
                 ) == 1 and all(a + b + c == 0 for a, b, c in set(zip(lst, lst[1:], lst[2:] + [0])))
```

The function takes a list of integers as input and returns True if three distinct elements in the list sum to zero, and False otherwise. It checks if there is exactly one triplet that sums up to zero and if all elements uniquely sum up to zero to return the required result.