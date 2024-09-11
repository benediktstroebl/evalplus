### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    :param n: An integer greater than 1 (not a prime)
    :return: The largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a simple trial division method to find the largest prime factor.

Here's a brief explanation of the algorithm:

1.  Start with `i = 2`, the smallest prime number.
2.  While `i * i` is less than or equal to `n`, check if `n` is divisible by `i`.
    *   If `n` is not divisible by `i`, increment `i` by 1.
    *   If `n` is divisible by `i`, divide `n` by `i` and repeat the process with the new value of `n`.
3.  Once `i * i` exceeds `n`, `n` is a prime number and the largest prime factor of the original input. Return `n`.

The script includes example usage at the end to demonstrate the function's behavior with the provided test cases.