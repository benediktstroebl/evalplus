```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2
    if max_even >= x and max_even <= y:
        return max_even
    elif max_even > y:
        return -1
    elif max_even < x:
        return -1
```

The function starts by finding the median of the two numbers, then checks if that median is an even number, and finally, checks if that even number is within the range of x and y. If the conditions are not met, -1 is returned.