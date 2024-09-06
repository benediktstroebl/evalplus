```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (symmetric) and the sum of its elements is less than or equal to the given maximum weight `w`. Otherwise, it will return False. The given examples in the problem statement would return the following results:
- `will_it_fly([1, 2], 5)` → False
- `will_it_fly([3, 2, 3], 1)` → False
- `will_it_fly([3, 2, 3], 9)` → True
- `will_it_fly([3], 5)` → True 

This function assumes that the input is a list of integers. If the input is not a list or contains non-integer elements, it may not return the expected results. 

It's always a good idea to handle edge cases and consider potential issues when solving coding challenges, but this code will at least provide a straightforward solution for the specified problem.