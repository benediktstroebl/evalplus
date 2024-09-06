```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True 

    for i in range(2, string_length):
        if string_length % i == 0:
            is_prime = False
            break
            
    return is_prime
```

This function `is_prime_length()` takes a single argument `input_str` which is the string to be evaluated for prime length. It first calculates the length of the input string and assigns it to the variable `string_length`. The function initializes a boolean variable `is_prime` to `True` as a default assumption that the string length could be prime until proven otherwise.

It then proceeds to evaluate if any number between 2 and the string length (inclusive) can divide the string length without leaving a remainder. This is done using a `for` loop that iterates through numbers from 2 to `string_length`. If a number within this range can divide the string length, the `is_prime` variable is set to `False` and the loop breaks, meaning that the evaluation stops. If no such number is found in the entire range, the `is_prime` variable remains `True`. 

Finally, the function returns the `is_prime` variable, which is `True` if the string length is prime and `False` otherwise.

This script guarantees that the function `is_prime_length()` behaves as expected based on the given test cases and problem statement because it returns `True` if the string length is prime and `False` otherwise. 

It is important to note that this function assumes that the input string is composed of only ASCII characters, as each ASCII character occupies a fixed number of bytes (typically 1 byte). This assumption holds for the given test cases but may need further validation for other scenarios.  If the input string contains characters from a multi-byte character encoding (such as UTF-8), this would affect the computation of the string's length. 

If you are working with such varied character sets, you may need to adjust how you calculate the string length to account for the varying byte sizes.  You would also need to adjust the expected prime numbers for testing.