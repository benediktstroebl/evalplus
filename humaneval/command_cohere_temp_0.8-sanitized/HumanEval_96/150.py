def is_prime(n):
    """Return true if n is a prime integer."""
    if n <= 1:
        return False
    for possible_divisor in range(2, int(sqrt(n)) + 1):
        if n % possible_divisor == 0:
            return False
    return True
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    prime_list = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            prime_list.append(i)
            count += 1
            if count == n: break
    return prime_list