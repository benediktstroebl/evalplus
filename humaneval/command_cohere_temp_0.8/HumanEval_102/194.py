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

The function employs a while loop to survey the range from `x` to `y` (inclusive), checking if each integer is even, and updating `max_even` if so. The loop will terminate once `temp` surpasses `y`, or if an even number exceeding `x` is encountered. 

Here is a test to validate the function:
```python
test_cases = [(12, 15, 14), (13, 12, -1)]
for x, y, expected in test_cases:
    assert choose_num(x, y) == expected
```

This provides a test case for all possible scenarios (where `max_even` is properly defined and returned, and when it is not). 
The `assert` statement ensures that the output of the `choose_num` function aligns with the expected outcome for each distinct input.