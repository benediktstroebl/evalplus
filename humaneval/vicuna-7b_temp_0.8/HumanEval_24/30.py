

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def dfs(n: int, i: int, divisor: int) -> bool:
        """
        dfs is a recursive function that finds the largest divisor of n by starting from the smallest
        divisor and moving up. It checks if divisor is in the list and if it is, it returns True
        indicating that the list is exhausted. Otherwise, it calls itself recursively.
        """
        if divisor == 1:
            return True
        if i == 0:
            return dfs(n, i, divisor)
        if n % divisor == 0:
            divisor = divisor // 2
            return dfs(n, i, divisor)
        return dfs(n, i + 1, divisor)

    divisor = 2
    result = dfs(n, 0, divisor)
    if result:
        return divisor
    else:
        return n // 2