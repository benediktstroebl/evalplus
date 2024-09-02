
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1

    # Since we are dealing with averages, we can round the answer
    # to the nearest integer
    avg = (n + m) // 2

    # We can also represent an integer as a binary number by first converting
    # it to a string and then using the built-in "bin()" function.
    binary_avg = bin(avg)

    # We can then remove the "0b" prefix and return the result
    return binary_avg[2:]

