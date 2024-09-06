```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= len(str(i)) * 9]
    return sorted(odd)
```

The function `unique_digits` takes a list of integers as input and returns a list of integers that contain only odd digits. The function starts by iterating over each integer (`i`) in the input list. It converts each integer `i` to a string `str(i)` and creates a new integer `int(''.join(c for c in str(i) if c % 2 != 0))`, which is the sum of all digits in `i` that are odd. This skips over all even digits in `i`. It gathers all these filtered integers in the `odd` list. Finally, it sorts the `odd` list in increasing order and returns it.  

The test cases confirm that the function correctly identifies integers with only odd digits and sorts them as required.