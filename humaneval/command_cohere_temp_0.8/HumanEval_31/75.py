```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
``` 

This function iterates from 2 up to n-1. Because the greatest factor of a number can only be one less than that number, it is guaranteed that the greatest factor will be found. The loop terminates at n-1 because any factor at this range or higher would have already been found in the previous iterations. 

Let's break down the tests and explain why they are true: 
1. `is_prime(6)` returns `False`. This returns false because 6 is divisible by 2 and 3. 
2. `is_prime(101)` returns `True`. This returns true because 101 is only divisible by 1, 3, 17, and 101. 
3. `is_prime(11)` returns `True`. This returns true because 11 is only divisible by 1 and 11. 
4. `is_prime(13441)` returns `True`. This number is a prime number because it is only divisible by 1 and itself. 
5. `is_prime(61)` returns `True`. This returns true because 61 is only divisible by 1, 3, 13, 19, and 61. 
6. `is_prime(4)` returns `False`. This returns false because 4 is divisible by 2. 
7. `is_prime(1)` returns `False`. This returns false because 1 is divisible by 1 and itself. 

This function is deterministic and efficient, reliably determining prime numbers with increasing complexity as the input size increases.