Here's the code:
```python
def pairs_sum_to_zero(l):
    s = sum(x) for x in l)
    if s % 2 == 0:
        return True
    else:
        return False
```

This function uses a generator expression to sum the elements of the list and then checks if the sum is even (0 or 2), which means the list has two elements that sum to zero. If the sum is odd, the function returns False, and if the sum is even, the function returns True.