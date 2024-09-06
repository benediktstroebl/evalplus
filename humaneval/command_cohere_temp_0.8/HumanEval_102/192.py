```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    return max(max_even, min_even) if max_even >= min_even and max_even % 2 == 0 else -1
```

The code works by finding the median value between `x` and `y` which is the biggest even integer in that range. It first calculates the maximum even number that is less than or equal to the median and the minimum even number that is equal to the maximum of `x` and `y` divided by 2. Then, it returns the maximum even number that is in the range if it is valid, meaning it is greater than or equal to the minimum even number and is even, and -1 otherwise. 

Here is a test suite that can be used to test the above function:
```python
# Testing choose_num function
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 4) == 2
    assert choose_num(3, 6) == 6
    assert choose_num(10, 10) == 10
    assert choose_num(11, 11) == 10
    assert choose_num(21, 21) == 18
    assert choose_num(22, 22) == -1
```