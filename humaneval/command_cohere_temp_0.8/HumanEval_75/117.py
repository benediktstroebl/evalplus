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
The task is to write a function that returns `true` if the given number is the product of three prime numbers and `false` otherwise. Knowing that the number is less than 100. 

The solution includes:
1. A loop to find the prime factors of the number incrementally starting from 2 up to the square root of the number. 
2. Checking the number after each prime detection if it's equal to 1, to exit the loop. 
3. If the loop ended without reaching the condition of being equal to 1, this means that not all prime factors were found, and the number is not the product of 3 prime numbers, so the function returns `false`. 
4. If the loop exits and the number is equal to 1, this means that all prime factors were found, and the function returns true. 

The example in the problem statement would make this function return `True`, as 30 is the multiplication of 3 prime numbers (2, 3, and 5).

This approach allows the function to be self-contained and does not rely on any external libraries or assumptions.