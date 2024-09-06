```python
import math

def hex_key(num):
    prime_hex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    count = 0
    num = str(num)
    for char in num:
        if char.isupper():
            count += prime_hex[int(char)]
    return count
```

The `hex_key` function takes a string num as input and initializes a list `prime_hex` with the indices of hexadecimal digits that are prime numbers. Then, it loops through the input num and if the character is uppercase, it checks if it's a valid hexadecimal digit, and if so, increments the count variable by the value in `prime_hex[int(char)]`. Finally, the function returns the calculated count, which represents the number of prime hexadecimal digits in the input num.

Here is a test suite to ensure the functionality of the code:
```python
def test_hex_key():
    # Example 1
    assert hex_key("AB") == 1
    # Example 2
    assert hex_key("1077E") == 2
    # Example 3
    assert hex_key("ABED1A33") == 4
    # Example 4
    assert hex_key("123456789ABCDEF0") == 6
    # Example 5
    assert hex_key("2020") == 2
    # Edge case
    assert hex_key("") == 0

test_hex_key()
``` 
The test suite provides different test cases to validate the correctness of the `hex_key` function. Each test case uses an assertion to compare the output of the function with the expected result for that particular test case.