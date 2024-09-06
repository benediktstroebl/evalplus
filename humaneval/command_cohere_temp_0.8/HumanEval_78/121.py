```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0

    # check if the number is empty or not a hexadecimal number
    if num == "":
        return 0

    # convert hexadecimal string to an integer to easily manipulate the digits
    num = int(num, 16)

    # count the prime digits by iterating through each digit of the number
    for digit in str(num):
        if digit in hex_digits and int(digit) in primes:
            prime_count += 1

    return prime_count
```

This script includes a list of prime numbers and hexadecimal digits to easily check if a digit is prime or not. The code assumes that the input is always correct, as stated in the assumption of the problem. 

The following is a test suite that can be used to validate the functionality of the code:
```python
# test the function with various inputs
test_cases = [
    ("AB", 1),
    ("1077E", 2),
    ("ABED1A33", 4),
    ("123456789ABCDEF0", 6),
    ("2020", 2)
]

for num, expected_result in test_cases:
    actual_result = hex_key(num)
    assert actual_result == expected_result, f"For input {num}, expected {expected_result}, but got {actual_result}."
```

To run the test suite, you can add the following code at the end of the script: 
```python
if __name__ == "__main__" :
    assert all(map(hex_key, test_cases)), "All test cases must pass"
```

This will run the test suite when the script is executed directly. 

```python
all(map(hex_key, test_cases))
```

The `all` function is used to check if all the results in the `map` function are true, so the expression is checked against multiple test cases. `map` applies the `hex_key` function to each entry in the `test_cases` list and returns a list of results, all of which are then checked by the `all` function.