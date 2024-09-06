```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y+1) if z % 2 == 0), default=-1)
    return max_even
```

The function 'choose_num' takes two positive numbers 'x' and 'y' as inputs and returns the largest even integer that falls within the range `[x, y]`, inclusive. If no such even number is found within the specified range, it returns -1 as per the problem statement. The built-in `max` function is used with a generator expression to find the largest even number, and the `default=-1` parameter ensures that if no valid even number is found within the range, it defaults to -1.