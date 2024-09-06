

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n_list = [1] + [2] * (n//2) + [1] + [3] * (n//3) + [1]
    while len(n_list) > 0:
        n_list.remove(max(n_list, key=lambda x: n % x))
    return n_list[-1]
