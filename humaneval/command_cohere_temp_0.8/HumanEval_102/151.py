```python
def choose_num(x, y):
    max_even = max(x, y) if (x == y) or ((x + y) & 1) else y
    return max_even if max_even <= max(x, y) else -1
```

The function 'choose_num()' takes two integers 'x' and 'y' as input, returns the maximum even integer less than or equal to the maximum of 'x' and 'y,' or returns -1 if no such even number exists. This solution utilizes the fact that the maximum even integer in the range is either the maximum of 'x' and 'y' or 'y' itself if the maximum of 'x' and 'y' is odd. Two variables, 'max_even' and `max(x, y)`, are compared using the `max()` function, and a conditional statement is used to determine which value to return based on the parity of the maximum.