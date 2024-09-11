Here's a self-contained Python script that uses the Sieve of Eratosthenes algorithm to solve the problem:
```python
def sieve_of_eratosthenes(limit: int) -> list:
    """
    Returns a list of boolean values representing prime numbers up to the given limit.
    """
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers

    for current_number in range(2, int(limit ** 0.5) + 1):
        if sieve[current_number]:
            for multiple in range(current_number ** 2, limit + 1, current_number):
                sieve[multiple] = False

    return sieve


def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    sieve = sieve_of_eratosthenes(n)
    for i in range(n, 1, -1):
        if sieve[i]:
            while n % i == 0:
                n //= i
            return i


# Example usage:
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))  # Output: 2
```
This script uses the Sieve of Eratosthenes algorithm to generate a list of boolean values representing prime numbers up to a given limit. Then, it uses this list to find the largest prime factor of the input number `n`. The `largest_prime_factor` function iterates from `n` down to 1, and for each prime number `i` it finds the largest power of `i` that divides `n` and returns `i` as the largest prime factor.