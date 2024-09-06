```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The Python script defines a function choose_num that takes two positive numbers x and y as input and returns the largest even integer that falls within the range of [x, y], inclusive. If no such even number exists in the given range, it returns -1. This behavior is achieved by employing a generator expression (z for z in range(x, y + 1) if z % 2 == 0), which creates a sequence of even numbers within the range [x, y+1]. The max function then determines the largest value in this sequence, while the default parameter -1 ensures that if no even number is found, the function returns -1. 

This approach guarantees that the function always returns the largest even number within the specified range, or -1 if no such number is present.