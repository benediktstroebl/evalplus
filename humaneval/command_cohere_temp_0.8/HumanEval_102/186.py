```python
def choose_num(x, y):
    max_even = -1
    i = x
    while i <= y:
        if i % 2 == 0:
            max_even = i
        i += 1
    return max_even
```

The function searches for even integers between `x` and `y`, and returns the maximum even number found, or -1 if none is found. This is achieved using a while loop that iterates through the integers between `x` and `y`, and checks if the current integer is even. The loop increments by 1, but it ensures that it will not exceed `y` during execution. 

This approach guarantees that the loop will terminate as it iterates up to `y` and stops incrementing when `i` reaches `y`. It also makes sure that the maximum even number in the range `x`, `y` is found and returned, or that -1 is returned if no even number is found in the range. 

The tests that can be used to confirm that the function works are: 

```python
# Testing a successful outcome
assert choose_num(12, 15) == 14
assert choose_num(2, 18) == 16

# Testing unexpected values
assert choose_num(13, 12) == -1
assert choose_num(0, 100) == -1
``` 

These tests cover multiple scenarios, from choosing the largest even number in a valid range to handling scenarios where there might not be an even number in the provided range.