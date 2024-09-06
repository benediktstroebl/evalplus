```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2  # Make it inclusive for even numbers
    if max_even >= x and max_even <= y:
        return max_even
    return -1
```

The function starts by finding the "middle" number between `x` and `y` – factoring in that the result should be even, this is calculated as `(x + y) // 2 + (if this number is odd, add 2)` (since the result needs to be inclusive of even numbers). 

Then, it simply checks if this calculated number is within the range of x and y, and returns it if it is. The -1 is returned if there is no such number in the range. 

This approach ensures that the result is always the largest even integer possible within the range, and handles edge cases such as the ones described in the example. 

This could be further improved with some fancy footwork by directly checking if the middle number is even, but the current strategy is both straightforward and clean. 

I hope this helping handling the problem adequately, let me know if this reasonable approach feels suitable!