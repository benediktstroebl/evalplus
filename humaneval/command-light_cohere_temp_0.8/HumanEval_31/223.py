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
This function is_prime uses a basic algorithm to check if a given number n is prime or not. It returns True if the start by checking if n is less than or equal to 1, which is definitely not prime. Then, it checks for divisibility by 2 and 3, returning False if either of these numbers divide n. The function then enters a prime candidate loop, where it uses the fact that all prime numbers greater than 3 are of the form 6k + 1, k being any integer greater than 0 but less than the square root of the number. 

The function then increases i by 1 and checks if n is divisible by i or i + 2. If it is, the function returns False, as the number is not prime. If n is not divisible by either i or i + 2, it has passed the prime candidate and is therefore prime, so the function returns True.