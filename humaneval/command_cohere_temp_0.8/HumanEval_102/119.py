```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even == min_even or max_even % 2 != 0:
        return -1

    return max_even
```

The Python script defines a function choose_num that fulfills the requirements of the given problem: taking two positive numbers x and y and returning the biggest even integer within the range [x, y] inclusive. The code first calculates the midpoint of the range and then checks if it is also the maximum possible even number. If not, it returns -1, indicating no even number exists in the range. Otherwise, it returns the maximum even number, ensuring it lies within the specified range.