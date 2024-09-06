Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    BIN_DIGIT_VAL = ['', '1']
    DIGIT_SUM = 0
    binary_string = ''

    while N > 0:
        DIGIT_SUM += N % 2
        N //= 2
        binary_string = str(DIGIT_SUM % 2) + binary_string
        DIGIT_SUM //= 2

    # Add an extra '0' if the DIGIT_SUM is an integer
    if DIGIT_SUM % 2 == 0:
        binary_string = '0' + binary_string

    # Convert binary string to an integer for the following logic
    int_binary = int(binary_string, 2)

    # Fill binary string with repeated '0' until it's a length of @BIN_DIGIT_VAL
    for i in range(len(BIN_DIGIT_VAL), len(binary_string)):
        binary_string = '0' + binary_string

    # Convert binary string back to a string of BIN_DIGIT_VAL
    binary_string = BIN_DIGIT_VAL[int_binary]

    return binary_string
```

This code defines the `solve` function, which takes a positive integer `N` as its argument and returns the total sum of its digits in binary. Here's a breakdown of the solution:
1. `BIN_DIGIT_VAL` is a list that contains the different values of a binary digit from 0 to its maximum length. In this case, it's initialized as an empty string and '1' since any real digit value is either 0 or 1.
2. An initial `DIGIT_SUM` variable is set to 0 and serves as a cumulative sum of the digits in the integer `N`.
3. A binary string `binary_string` is initialized as an empty string and will be filled as we iterate through the digits of N.
4. While `N` is greater than 0, we calculate the remainder of N divided by 2 and add it to `DIGIT_SUM`. We then divide N by 2 and append the DIGIT_SUM to the `binary_string`. Afterward, we divide `DIGIT_SUM` by 2 to be ready for the next iteration.
5. After the iterations, if `DIGIT_SUM` is even, we add an extra 0 to `binary_string` to account for the possibility that `DIGIT_SUM` has an even number of binary digits.
6. The code then converts `binary_string` to an integer using `int(binary_string, 2)`.
7. To handle any mismatches in the length of `binary_string` and `BIN_DIGIT_VAL`, the code fills `binary_string` with repeated 0s up to the length of `BIN_DIGIT_VAL` using a `for` loop.
8. Finally, we convert `binary_string` back to a string of `BIN_DIGIT_VAL` using its integer representation and return the result.