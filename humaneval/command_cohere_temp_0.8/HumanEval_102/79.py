```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that exists in the range between them. The loop starts from `x` and iterates upwards until it reaches `y`. During each iteration, it checks if the current number is even, and if so, it updates `max_even` with the current number if it's bigger than the previous `max_even`. If no even number is found in the range, it will return -1. This approach takes advantage of the symmetry of the problem and avoids the need for explicit symmetry checks.  This makes the code more efficient and easier to understand.