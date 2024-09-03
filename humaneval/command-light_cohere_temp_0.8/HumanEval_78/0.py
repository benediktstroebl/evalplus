```python
def hex_key(num):
    """
    Determine the number of prime hexadecimal digits in the given string.
    If the string is assumed to only contain uppercase letters, and empty.
    Initialize counter of primes and count = 0
    for c in num:
        if c in '23456789ABCDEF':
            count += 1
        else:
            break
    return count

# Test cases
test_case1 = "AB"
test_case2 = "1077E"
test_case3 = "ABED1A33"
test_case4 = "123456789ABCDEF0"
test_case5 = "2020"

# Test function
def test():
    expected = 6
    actual = hex_key(test_case4)
    assert actual == expected

# Run the function and test cases
test()
test_hex_key()
```
This script defines a function `hex_key` that calculates the number of prime hexadecimal digits in a given string. The `test` function verifies the expected output against the `hex_key` function's actual output.