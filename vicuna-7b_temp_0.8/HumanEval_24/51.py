

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    largest = n
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                divisors.append(i)
                while n % i == 0 and n >= largest:
                    largest = n
                if largest != n:
                    break
        n -= 1
    return largest
