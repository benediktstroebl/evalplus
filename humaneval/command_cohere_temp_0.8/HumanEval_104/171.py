```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(n) if c % 2 != 0)) for n in x if int(''.join(c for c in str(n) if c % 2 != 0)) <= n]
    return sorted(odd)
```

The algorithm for this solution is simple:
1. Create a list of odd digits string using list comprehension and `str(n)`.
2. Filter out the numbers whose odd digitless strings are greater than the original number.
3. Sort the list and return it. 

This algorithm efficiently solves the problem in a single sweep without the need for multiple iterations.