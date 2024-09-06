ALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(n: int) -> bool:
    """Check if an integer is prime."""
    if n < 2:
        return False
    for possible_divisor in range(2, int(n**0.5) + 1):
        if n % possible_divisor == 0:
            return False
    return True
def count_up_to(n: int) -> list:
    """Return the first n prime numbers less than n."""
    ans = []
    check_up_to = n - 1
    for num in ALL_PRIMES:
        if is_prime(num) and num <= check_up_to:
            ans.append(num)
            if len(ans) == n:
                break
    return ans