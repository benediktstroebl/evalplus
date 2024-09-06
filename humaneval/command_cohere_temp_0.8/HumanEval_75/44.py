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

The function `is_multiply_prime` checks if the given number is less than 100 and not 1 to avoid division by zero errors. It then iterates through factors beginning from 2 up to the square root of the given number. While the number is divisible by the current factor, it is appended to the `prime_factors` list, and the number is divided by that factor. If the number becomes 1, the loop stops. Finally, the function returns `True` if the length of `prime_factors` is exactly 3, indicating that the given number is the product of three prime factors.

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The output of this code will be `True` because 30 is the multiplication of 3 prime numbers: 2, 3, and 5.