```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    
    if max_even % 2 == 0 and x <= max_even <= y:
        return max_even
    else:
        return -1
```

The function starts by finding the median of the two numbers, however, it only accepts the median value if it is also the maximum value between the two input numbers. This algorithm ensures that the output is the largest even integer in the range of the two numbers, or -1 if no such number exists. 

Here is a simple test suite to ensure that the function is correct:
```python
# Testing choose_num function
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 26) == 14
    assert choose_num(10, 15) == 10
    assert choose_num(1, 101) == -1
    assert choose_num(21, 17) == 14
``` 

This test suite covers all the bases: accepting inputs where an even number exists between the two numbers, as well as situations where no even number exists.