import unittest
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char != ' ':
            if char <= '9' and int(char) % 2 == 0:
                even_count += 1
            elif char <= '9' and int(char) % 2 != 0:
                odd_count += 1
    return even_count, odd_count