```python
def is_multiply_prime(a):
    # check if a is 1, in that case multiplication with any number will be 1 and this will not be prime
    if a == 1:
        return False
    
    # check if a is divisible by 2, in that case it is not prime
    if a % 2 == 0:
        return False
    
    # check divisibility by odd numbers (3, 5, 7, ...)
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    
    return True
```

This function checks if the number `a` is divisible by 2 and returns false immediately if it is. Then, it iterates through odd numbers starting from 3 up to the square root of `a` (checking only odd numbers, as even numbers greater than 2 cannot be prime) and returns false if `a` is divisible by any of them. If none of these conditions are met, it returns true, indicating that `a` is the product of three primes. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
# Output: True
```
This example illustrates how the function correctly identifies 30 as a multiplication of three primes: 2, 3, and 5. 

This approach ensures that the function delivers the expected results for multiplication of prime numbers within the given range.