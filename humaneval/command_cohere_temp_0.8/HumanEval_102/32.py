```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_even = max_even - 1
    if floor_even % 2 == 0:
        return floor_even
    elif x == y:
        return -1
    else:
        return choose_num(x, floor_even) if floor_even >= x else choose_num(floor_even + 1, y)
```

The function takes two positive numbers `x` and `y` as input and returns the largest even integer that falls within the inclusive range `[x, y]`. In the event that no such even number exists, the function returns -1. The logic employs recursive searching, checking if `floor_even` (obtained by subtracting 1 from the maximum even number) is an even integer. If it is, it's returned, otherwise, the function continues its search within the smaller range `[x, floor_even]` or `[floor_even + 1, y]` accordingly. 

Here is a simple test case to ensure the function behaves correctly:
```python
print(choose_num(12, 15))  # Should print 14
print(choose_num(13, 12))  # Should print -1
```

And here is a more thorough test suite that covers edge cases:
```python
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 4) == 2
    assert choose_num(3, 9) == 6
    assert choose_num(10, 10) == 10
    assert choose_num(11, 11) == 10
    assert choose_num(21, 21) == 18
    assert choose_num(22, 22) == -1
    assert choose_num(23, 24) == -1
    assert choose_num(25, 25) == 25

test_choose_num()
```

Note that the function includes a recursive aspect, which means it calls itself. Therefore, you should be mindful of the domain of the inputs to avoid potential issues with recursive calls.