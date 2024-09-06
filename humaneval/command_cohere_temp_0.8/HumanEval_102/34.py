```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even & 1
    return max_even if max_even <= max(x, y) else -1
```

The function starts by finding the median of the range with integer arithmetic, rounding up if the median is odd. It then returns the median if it's within the range [x, y], or -1 if not. This solution efficiently handles all cases in O(1) time.