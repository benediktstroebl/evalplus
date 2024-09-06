```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even:
        return -1
    else: 
        return choose_num(max_even, min_even)
```

The code defines a function choose_num, which takes two positive numbers x and y as input and returns the largest even integer that falls within the range of [x, y], inclusive. If no such even number is found within this range, it returns -1. The algorithm employs a recursive approach, exploring both the maximum and minimum values of even numbers in the given range to efficiently pinpoint the largest even number. 

Here is a simple test suite to ensure the functionality of the code:
```python
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 11) == 10
    assert choose_num(21, 23) == 22
    assert choose_num(26, 17) == -1
```