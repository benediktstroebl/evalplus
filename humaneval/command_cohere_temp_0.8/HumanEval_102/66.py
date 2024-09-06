```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y+1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulo check of even numbers to find the biggest even number in the range `[x, y]` (`z for z in range(x, y+1) if z % 2 == 0`). The `max()` function works on generators as well as lists and returns the biggest even number in the range, or `-1` if no even number is found. 

To validate the solution, you can create a test module with functions that assert the behavior of the `choose_num` function for different input scenarios:
```python
def test_choose_num():
    # Biggest even number in the range [x, y]
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1

    # Edge cases
    assert choose_num(1, 3) == 2
    assert choose_num(0, 100) == -1
    assert choose_num(100, 0) == -1
    assert choose_num(25, 25) == 24
```

This way, the `choose_num` function can be reused and easily incorporated into larger projects.