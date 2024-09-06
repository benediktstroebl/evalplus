```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
``` 
This function uses the trial division method with some optimizations to determine if a number is prime or not, it first excludes the less than 2 numbers and then uses a optimized approach to test for primality by looking for divisibility in consecutive numbers starting from 5. 
This implementation runs in O(n) time complexity and is suitable for larger inputs.