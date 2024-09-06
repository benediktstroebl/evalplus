```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    while temp_num <= y:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num += 1
    return max_even if max_even != -1 else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
```

This Python script defines the `choose_num` function, which takes two positive numbers `x` and `y` as input and returns the largest even integer that falls within the range `[x, y]`, inclusive. If no such even number is found within this range, it returns -1. 

The function iterates through the numbers starting from `x` within the provided range, checking if each number is even. The largest even number encountered is stored in the variable `max_even`, and if no even number is found, `max_even` remains -1. The function then returns the value of `max_even` to provide the desired result.

The script includes two test cases that verify the function's behavior for the given examples from the problem statement: It correctly returns 14 for the first example (where the largest even number between 12 and 15 is 14) and returns -1 for the second example (since there is no even number between 13 and 12).