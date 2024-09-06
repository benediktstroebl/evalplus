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

The function begins by finding the midpoint between `x` and `y` and checks if it is an even number and within the range. If so, it returns this maximum even number. If not, it returns -1. You can test this function using the examples in the prompt.