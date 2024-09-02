from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    def check(n, p, factors):
        if n == 0:
            return True, 1
        for i in range(1, n + 1):
            if n % i == 0:
                return False, 0
        return True, n

    def dfs(n, factors, visited):
        if n in visited:
            return visited[n]
        if n == 1:
            visited[n] = factors
            return factors
        for i in range(1, n):
            if n % i == 0:
                factor = factor * i
                new_factors = dfs(factor, factors, visited)
                factors.append(factor)
                visited.append(factor)
                return new_factors
        return None

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if not factors:
        return None

    visited = [None] * (n + 1)
    result = []
    visited[n] = None
    for p in factors:
        if p not in visited:
            factors.remove(p)
            result.append(p)
            remaining = n // p
            visited[remaining] = None
            for q in factors:
                if q not in visited and q > remaining * 2:
                    result.append(q)
                    factors.remove(q)
    return result

