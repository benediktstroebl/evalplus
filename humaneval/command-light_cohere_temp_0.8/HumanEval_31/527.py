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
This function is designed to determine whether a given number n is a prime, following a basic algorithm. 

It first checks for numbers less than or equal to 1 and less than 3, as these are not prime. It then checks for the most common factor, which is 2 and 3, by checking divisibility. 

The function then enters a loop that checks for divisibility by consecutive odd numbers, up to the square root of the number.