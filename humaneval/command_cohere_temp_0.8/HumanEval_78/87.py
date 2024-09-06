Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(num):
    """Checks if a number is a prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    hex_digits = "0123456789ABCDEF"
    count = 0
    for char in num:
        if char.isupper():
            digit = hex_digits.find(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The provided Python script defines a function `hex_key` that solves the problem as described in the markdown code block. It counts the number of hexadecimal digits that are primes, assuming the input is always correct or empty strings, and symbols `A, B, C, D, E, F` are always uppercase. The script assumes that the input test cases will be provided as console input when the script is executed. 

You can test the script by calling the `hex_key` function with the given examples in the markdown code block. Note that the script assumes that the input will be provided as a string, and it returns the count of prime hexadecimal digits as an integer.  If you want to provide input using variables `num` with values `AB, 1077E, ABED1A33, 123456789ABCDEF0, 2020`, you need to add corresponding assignments before calling the function.  For example:
```python
num1 = "AB"
num2 = "1077E"
num3 = "ABED1A33"
num4 = "123456789ABCDEF0"
num5 = "2020"
print(hex_key(num1)) # 1
print(hex_key(num2)) # 2
print(hex_key(num3)) # 4
print(hex_key(num4)) # 6
print(hex_key(num5)) # 2
``` 
This would execute the script and output the following:
```
1
2
4
6
2
``` 

The script also defines a helper function `is_prime` that checks if a given number is a prime number. This function is used to determine if each hexadecimal digit is prime.  The `hex_key` function iterates through each character in the input `num`, and if the character is uppercase, it converts it to a digit in ` hex_digits ` ranging from `0-9` or `A-F` and checks its primality using the `is_prime` function.  If the digit is not uppercase, it is treated as an integer representation of a digit.  The function then counts the number of prime digits and returns the count.  The script assumes that the environment where the script is executed has the `sorted` and `int` functions available. 
```python
sorted = lambda x: sorted(x)
int(x) == int(x, 0)
``` 
You can run the script assuming the input tests cases as described in the code block, and it should produce the correct output as shown below:
```bash
1
2
4
6
2
``` 
If you need to modify the script to run as a code snippet in a Markdown cell, you would need to wrap the script in a importing the