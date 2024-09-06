```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(int(rounding(n)) ** 2 for n in lst for rounding in (lambda x: x, lambda x: x + 0.5, lambda x: x - 0.5) if int(rounding(n)) ** 2)
    return result
```

The code works by iterating over each number in the input list. For each number, it applies three rounding functions (round, round + 0.5, round - 0.5) to determine whether it rounds up, down, or remains the same when rounded to the nearest int. Then, it calculates the squared value for the corresponding rounded integer and contributes that to the sum. Ultimately, it returns the calculated sum of squared values.

This solution is efficient with time complexity O(n^2), owing to the nested iteration over the list lst and rounding iterations.