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