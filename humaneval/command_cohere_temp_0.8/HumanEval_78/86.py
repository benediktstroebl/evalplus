```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # check for incorrect symbols and numbers that are not hexadecimal
    if re.search(r'[^A-Fa-f0-9]', num):
        return "Invalid hexadecimal number"

    for char in num:
        if char in hex_digits:
            digit = hex_digits.index(char)
            if primes[digit]:
                count += 1

    return count
```

The problem is solved by utilizing a list of prime numbers up to 50, and a list of hexadecimal digits. The script creates an index for hexadecimal digits, then loops through each digit in the provided hexadecimal number, and checks whether it is prime. If the digit is prime, it is incremented in the count variable and returned as the final answer. 

The code includes basic error handling to ensure the input is a string of valid hexadecimal digits, and returns an error message if this is not the case. Let's break down the code step by step:
- The `re` module is imported at the beginning of the script, which allows the user to search for strings that match a particular pattern using regular expressions. 
- The `hex_key` function takes a single argument, num, which is the hexadecimal number you want to check.
- `primes` is a list of prime numbers up to 50, which is used to check the primality of each digit in the hexadecimal number. 
- `hex_digits` is a list of all hexadecimal digits. This is used to convert each digit in `num` to its corresponding integer value.
- `count` is a variable that keeps track of how many digits in the hexadecimal number are prime. It is set to 0 at the beginning of the function. 
- The code checks that the input is a string of valid hexadecimal digits using `re.search`, and returns an error message if this is not the case. 
- For each character in `num`, it is checked whether it is present in the `hex_digits` list. If the character is a hexadecimal digit, its index in the `hex_digits` list is found using `hex_digits.index(char)`. This gives the integer representation of the digit (for example, 'A' is converted to 10, 'B' to 11, and so on).
- If the digit is prime (i.e., it is present in the `primes` list at the index determined above), it is added to `count`. 
- Finally, `count` is returned as the number of prime hexadecimal digits in the provided number. 

Overall, the code provides a clean and efficient solution to the problem, and can be easily plugged into a markdown code block. Feel free to ask any questions or modify the code to better fit your needs.