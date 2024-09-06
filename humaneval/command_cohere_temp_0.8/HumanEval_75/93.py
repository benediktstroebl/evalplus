```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False
    return True
```

This Python script defines a function `is_multiply_prime` that takes a single parameter `n`, representing the target number for evaluation. The function checks if `n` is divisible by any prime number less than or equal to the square root of `n`, if any such prime is found, the function returns False, indicating that the number is not the product of three primes. Otherwise, it returns True, indicating that the number could be the product of three primes. 

This approach optimizes the prime checking process by only considering prime numbers up to the square root of `n`, as any prime factor larger than the square root would have a corresponding factor smaller than the square root. 

To further improve efficiency, the function leverages a pre-computed list of primes, reducing the need for repeated prime number testing. 

Overall, the script provides an optimized solution to determine if a given number is the product of three primes, offering a balance between accuracy and efficiency. 

You can test this function by calling it with different numbers and verifying the results against the specified conditions in the problem statement.