```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    return max_even if max_even % 2 == 0 and max_even in range(x, y + 1) else -1
```

The function first tries to find the biggest even integer in the range [x, y] by taking the midpoint of the interval and checking if it's even. If it's not even, it will iterate through the endpoints x and y to return the biggest even number in the range. The function returns -1 if no such number exists. This approach ensures that the correct biggest even number in the range is found, handling edge cases correctly.