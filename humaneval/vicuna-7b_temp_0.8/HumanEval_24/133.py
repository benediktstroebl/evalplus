

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    max_divisor = min_index = 0
    for i in range(1, n+1):
        for j in divisors:
            if j % i == 0:
                if j > n:
                    break
                else:
                    max_divisor = j
                    max_index = j // i
                    min_index = max_index
    return max_index
