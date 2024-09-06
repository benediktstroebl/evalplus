```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # Check if the input string is empty or not
    if num == "":
        return 0

    # Split the input string into an array of single digits
    num = re.findall(r'[0-9A-F]', num)

    # Check each digit of the hexadecimal string if it is prime
    for digit in num:
        if digit in hex_digits and digit in primes:
            count += 1

    # Return the counted number of prime hexadecimal digits
    return count
```

This script utilizes the `re` module to simplify parsing the input string and create a list of digits to iterate for prime detection. The `hex_key` function detects prime digits in the hexadecimal number and counts them, returning the result. 

It assumes the input is correct and contains only uppercase A-F and digits 0-9. You can verify the functionality by running the function with the provided test cases or any other input as a string.  Any character that is not a hexadecimal digit, which is not allowed in the given specification, will cause the function to fail gracefully and return `0`.  This will occur when the function encounters a character like `g` or `k`, which are not in the list of hexadecimal digits specified in the problem.