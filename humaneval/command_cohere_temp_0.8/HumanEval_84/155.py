Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    BIN_DIGIT_VAL = [0, 1]
    SUM_IN_BIN = 0
    DIGITS = [int(d) for d in str(N)]
    
    for digit in DIGITS:
        SUM_IN_BIN += BIN_DIGIT_VAL[digit % 2]
        
        if SUM_IN_BIN > 1:
            return '1'
        
        BIN_DIGIT_VAL.append(BIN_DIGIT_VAL[digit % 2] + BIN_DIGIT_VAL[digit % 2 + 1])
    
    return '0' if SUM_IN_BIN == 0 else '1'
```

The provided Python script implements a function called `solve(N)` that takes a positive integer `N` as input. This function calculates the total sum of the binary digits of `N` and returns the binary representation of this sum.

Here's how it works:
- `BIN_DIGIT_VAL` is a list that stores the binary digits '0' and '1'.
- `SUM_IN_BIN` is initialized to 0 and will hold the binary sum of the digits of `N`.
- `DIGITS` is a list that contains the individual digits of the integer `N`, converted to integers.
- A loop iterates through each digit in `DIGITS`. For each digit, it adds the appropriate binary value to `SUM_IN_BIN` (i.e., '0' for even digits, '1' for odd digits).
- After each iteration, it checks if `SUM_IN_BIN` is greater than 1. If it is, the function returns '1' immediately because a '1' in the binary representation means that the sum of digits is greater than 1.
- If `SUM_IN_BIN` is not greater than 1, the script proceeds to the next iteration.
- Outside the loop, it checks if `SUM_IN_BIN` is 0. If it is, the function returns '0' because there are no digits to sum. Otherwise, it returns '1'.

This algorithm efficiently computes the binary representation of the sum of the digits of `N` in a single pass.