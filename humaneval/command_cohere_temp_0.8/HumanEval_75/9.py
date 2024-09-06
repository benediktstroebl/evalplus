```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a**0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```
The task is to write a function that returns `true` if the given number is the product of three prime numbers and `false` otherwise. To do so, the function determines all prime factors of the number, and returns `true` if there are exactly three of them. The code uses an iterative approach to determine prime factors, ensuring a efficient and optimized implementation.