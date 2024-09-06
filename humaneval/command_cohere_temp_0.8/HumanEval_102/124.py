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

The code uses a `while` loop to iterate through numbers between `x` and `y` (inclusive), checking if each number is even. The `max_even` variable is used to track the largest even number found during the iteration. The loop continues until the next number would be greater than `y`, ensuring that all eligible even numbers in the range are considered. The final value of `max_even` is returned if it is not -1, indicating that no eligible even number was found. 

Here is a test to ensure the function `choose_num` works as expected:
```python
test_choose_num = '''
# Testing choose_num function

assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 10) == 8
assert choose_num(100, 200) == 198
assert choose_num(101, 200) == -1
'''
``` 
This test covers different scenarios and verifies that the function behaves as expected, returning -1 when there is no even number in the given range and correctly identifying the largest even number when it exists.