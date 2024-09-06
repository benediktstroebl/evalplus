```python
import math

def hex_key(num):
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in hex_digits and int(digit) in prime_list:
            count += 1
    return count
```

The `hex_key` function takes a string num as input and counts the number of hexadecimal digits that are primes. The function first creates a list of prime numbers from 2 to 20 and then loops through the input number num and counts the number of digits that are in the list of prime numbers and the hexadecimal digits. The function returns the number of counted digits.

This solution focuses on the prime checking part of the problem, so the rest is just converting the input to integers and looping through the digits.

Here is a test suite to see if the function is correct:
```python
# Test Suite
def test_hex_key():
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2

test_hex_key()
```

With these tests, you can assure that the function works correctly.  The total time complexity of this solution is O(nm), where n is the number of digits of the given hexadecimal number and m is the maximum number of iterations for the for loop that is checking for the prime digits.  This is a practical solution and the time complexity is proportional to the number of digits and the maximum number of iterations.  Also, this solution is infinitely more efficient than trying to iterate over every single digit and every possible combination of digits, which would lead to a time complexity of O(n^2^).  This solution is also reasonably efficient in terms of the space complexity since it only creates one extra list for the prime digits, so the space complexity is O(k), where k is the size of the list of prime digits.  This is a very efficient solution in practice.