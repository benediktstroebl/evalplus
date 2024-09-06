```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y+1) if z % 2 == 0), default=-1)
    return max_even
```

The logic for the function is as follows:
1. We use `max` along with a generator expression to find the biggest even number in the range [x, y+1]. The `default=-1` argument ensures that if no even number is found in the range, the max function will return -1.
2. The generator expression `(z for z in range(x, y+1) if z % 2 == 0)` creates a generator that iterates over all integers z in the range `[x, y+1]`, and only includes those integers whose parity is even. The biggest number in this generator is then found through the use of the max function, with a default value (-1) in case there are no even numbers in the given range. 

The generator expression in the max function is a concise way to filter even numbers from the range without having to introduce an additional loop. Thus the function is both efficient and readable. 

This solution should be robust and adaptable to edges cases like empty intervals or scenarios where even numbers are not present.