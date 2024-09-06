```python
import math

def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for digit in digits:
        if digit in num and is_prime(int(digit)):
            count += 1
    return count
```

The key function in this code is the `is_prime` function, which checks whether a given number is prime. It iterates through the numbers from 2 to the square root of the input number and checks whether the input number is divisible by any of them. If it is, the function returns `False`, indicating that the number is not prime. If the loop completes without finding a divisor, the function returns `True`, indicating that the number is prime. 

The `hex_key` function uses `is_prime` to check each digit of a hexadecimal string `num`. It loops through each digit ('0' to 'F'), and if the digit is present in `num` and is prime, it increments the `count` variable. Finally, it returns the total count of prime digits. 

To test this code, you can use the following test cases:
```python
# Testing the is_prime function
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False
assert is_prime(9) == False
assert is_prime(10) == False

# Testing the hex_key function
assert hex_key("AB") == 1
assert hex_key("1077E") == 2
assert hex_key("ABED1A33") == 4
assert hex_key("123456789ABCDEF0") == 6
assert hex_key("2020") == 2
```

These test cases cover a range of input scenarios, including edge cases, to ensure that both the `is_prime` and `hex_key` functions work correctly.  This will help ensure that the function behaves as expected in different cases. 
If you encounter any issues or have further questions, feel free to ask! I'll be glad to assist you in understanding and improving the code.