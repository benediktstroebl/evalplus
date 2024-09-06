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

The function starts by finding the midpoint between `x` and `y`. It then updates the max even number possible within the range to either the midpoint, `x`, or `y` whichever is the largest. Afterward, it checks if the max even number is within the range `[x, y]` and is also even, and returns the number if the criteria are met; otherwise, it returns -1. 

The function assumes that `x` and `y` are both positive numbers, and the domain of the function is solely focused on positive integers.