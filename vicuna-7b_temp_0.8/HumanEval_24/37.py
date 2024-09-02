

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    while len(divisor_list) < n:
        divisor_list.append(max(divisor_list) + 1)
    return divisor_list[-1]
