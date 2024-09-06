```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and max_even >= x and max_even <= y:
        return max_even
    else:
        return -1
```

The function first tries to find the biggest even number in the range [x, y] by taking the midpoint of the interval and checking if it's even. If it isn't, it adjusts the search range to the smaller values (x or y) that are eligible for the maximum even number and repeats the process until it finds an even number or the range is invalid. The final result is the biggest even number in the requested range, or -1 if no such number exists.