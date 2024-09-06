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
This code defines a function called is_prime that checks whether a given number n is a prime or not. It uses a basic and efficient prime checking methods:
- If n is less than or equal to 1, it's not prime.
- If n is 2 or 3, it's prime.
- If n is even 2 or 3, it checks for divisibility, and if divisible, it returns False.
- It then starts a loop from 5 (why 5? Inside the loop, it checks for divisibility by i and i + 2. If n is divisible by either of these values, it returns False. Otherwise, it continues to the next iteration with i += 6, and so on.

This function passes all the provided tests and can be used to determine whether a given number is prime or not.