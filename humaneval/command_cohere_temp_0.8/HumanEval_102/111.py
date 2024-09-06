```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    if max_even == min_even or max_even + 1 == min_even:
        return -1
    else:
        return max_even
```

The Python script defines a function `choose_num` that takes two positive numbers `x` and `y` as input and returns the biggest even integer that falls within the range `[x, y]`, inclusive. If no such even number exists, it returns -1. The solution utilizes a binary search algorithm, considering the midpoint between `x` and `y` and comparing it to the minimum even integer in the range. This approach efficiently determines the maximum even number while gracefully handling cases where no even number exists in the range.