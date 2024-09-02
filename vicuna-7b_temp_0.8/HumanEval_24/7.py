

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def dfs(n, i):
        if n == 0:
            return []
        if n == 1:
            return [i]
        result = []
        for j in range(i, n):
            if j % i == 0:
                result.append(j)
            if j % i == -1:
                result.append(n - j)
        dfs(n, i + 1)
        dfs(n, i - 1)
        return result
    return max(dfs(n, 2))
