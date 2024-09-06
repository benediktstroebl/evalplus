Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Checks if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Counts the number of hexadecimal digits that are primes."""
    digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = digits.find(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The code solves the problem by first creating a method `is_prime` that checks if a given number is prime. Then the `hex_key` function goes through each character in the hexadecimal string `num` provided and determines if the character is an uppercase letter or a digit. If it is a letter, it transforms it into a digit using the `digits.find(char)` method. If the char is already a digit, it proceeds with the checking using the `is_prime` method. It increments the counter if the digit is prime. Finally, it returns the count of prime digits. 

This solution works for all cases as stated in the problem statement. You can test this code by providing different inputs to the `hex_key` function. 

Here is an example of how to use the `hex_key` function:
```python
print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2
```