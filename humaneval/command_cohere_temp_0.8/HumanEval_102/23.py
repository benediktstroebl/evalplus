```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The function chooses the biggest even number that is in the range between `x` and `y`. It initializes `max_even` with the value `-1` and then loops through the range from `x` to `y` (inclusive) checking if each number is even. If a number is even, it becomes the new maximum even number found so far (`max_even`). The loop continues until the next number would be greater than `y`, ensuring that every even number in the range is checked. 

Here's a simple test suite to ensure the function behaves as expected:
```python
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 4) == 2
    assert choose_num(10, 10) == 10
    assert choose_num(0, 5) == 0
    assert choose_num(7, 10) == -1
```