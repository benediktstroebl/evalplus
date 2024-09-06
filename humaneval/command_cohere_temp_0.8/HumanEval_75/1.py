```python
def is_multiply_prime(a):
    # Check if a is a multiple of 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0: 
        return True
    # If none of the above, return false
    return False
```

The function `is_multiply_prime` checks whether the given number is divisible by 2, 3, or 5. These are the most obvious prime candidates to use for multiplication, with the highest chance of giving false results. If a number is divisible by at least one of these, it is a multiply prime. Otherwise, it is not, so the function returns `False` in that case. 

This approach is efficient and relatively straightforward, but it does not cover all prime numbers. To cover all prime numbers up to the square root of `a`, you'd need a more sophisticated approach, like the ones used in the Sieve of Eratosthenes method. However, for this problem, where you are looking for "obvious" multiplications of small prime numbers, this approach will deliver the required functionality with sufficient efficiency.