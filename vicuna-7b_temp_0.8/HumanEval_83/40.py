
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Store each digit of n as an array
    digits = [list(str(d)) for d in n]
    # Store each digit as an array
    digits_arr = [[0] * 10 for _ in range(len(digits))]
    # Iterate through each digit in n
    for i, d in enumerate(digits):
        # Add 1 to the leftmost digit
        digits_arr[0][i] += 1
        # Add 1 to the rightmost digit
        digits_arr[-1][i] += 1
        # If the leftmost digit is 1 and the rightmost digit is 1, increment the count
        if d == '1' and digits_arr[-1][i-1] == 1:
            digits_arr[-1][i] += 1
    # Return the count
    return sum(d[0] for d in digits_arr)
