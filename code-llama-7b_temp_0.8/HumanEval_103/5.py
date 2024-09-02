
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
    # Initial check
    if n < m:
        return -1
    if n == m:
        return n
    # Compute the average
    avg = (n + m) / 2.0
    # Round the average
    avg = round(avg)
    # Convert the average to a binary string
    avg_bin = bin(int(avg))
    # Replace "0b" with "0b1" to ensure that the binary string is non-negative
    return "0b" + str(avg_bin).replace("0b", "")
