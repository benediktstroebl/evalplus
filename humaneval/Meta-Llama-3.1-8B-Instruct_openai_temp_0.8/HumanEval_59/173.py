### Largest Prime Factor Function
#### Description
This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given integer `n`.

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: Input integer
    :return: Largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

### How it works

1. The function starts with a variable `i` initialized to 2, the smallest prime number.
2. It then enters a while loop that continues as long as `i` squared is less than or equal to `n`.
3. Inside the loop, it checks if `n` is divisible by `i`. If it's not, `i` is incremented by 1.
4. If `n` is divisible by `i`, `n` is divided by `i` to remove this factor from `n`.
5. The loop repeats until `i` squared is greater than `n`.
6. At this point, `n` contains the largest prime factor of the original input `n`, which is then returned as the result.

This function has a time complexity of O(√n) and a space complexity of O(1), making it efficient for large inputs.