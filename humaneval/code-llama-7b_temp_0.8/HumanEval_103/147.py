
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
    # Tip: Use the // operator for integer division.
    # Tip: Use the % operator to compute the remainder.
    # Tip: The round() function rounds a number to the nearest integer.
    # Tip: You can convert integers to binary using the bin() function.
    if n > m:
        return -1
    else:
        avg = round((m+n)/2)
        return bin(avg)

