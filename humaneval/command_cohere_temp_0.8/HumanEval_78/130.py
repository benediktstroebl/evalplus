```python
import math

def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    if not num:
        return 0
    digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in digits and is_prime(int(digit)):
            count += 1
    return count
```

The solution makes use of the `is_prime` function to check if a number is prime. For each digit in the hexadecimal number, it converts it to an integer and checks if it is prime. It increments the counter if it is. The final count of prime digits is then returned.

To determine if a number is prime, the `is_prime` function runs a loop from 2 to `int(n**0.5) + 1`. During each iteration, it checks if the number is divisible by the current integer. If the number is divisible by any integer within this range, it returns `False`. If it is not, it returns `True`. 

Note that the `is_prime` function's implementation is not optimal for large numbers, as it uses a linear approach with a loop and could benefit from using more efficient prime-checking algorithms like the Sieve of Eratosthenes. However, for this problem, which deals primarily with small hexadecimal digits, it provides a straightforward solution. 

The `hex_key` function calls `is_prime` for each digit in the provided hexadecimal number, counting the number of primes and returning the total. 

The code above adheres to the problem's assumption that the input is always correct or empty, and it treats symbols as uppercase. It also assumes that the input string contains only hexadecimal digits and no other characters. 

The total time complexity of this code is O(k * log(k)), where k is the number of digits to be checked. 

You can use this code by directly calling the `hex_key` function and passing in the desired hexadecimal number as a string. You can further augment this code to handle a list of hexadecimal numbers, returning a single integer count of all prime digits in the list, by adjusting the arguments passed to `hex_key` and using a list comprehension.