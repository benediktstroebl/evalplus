

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def divide(divisor: int) -> bool:
        return not n % divisor

    def find_largest(start: int, end: int) -> int:
        if end - start < 0:
            return None
        if start == end:
            return start
        return max(find_largest(start + 1, end), find_largest(start, end - 1))

    return find_largest(1, n // 2)

