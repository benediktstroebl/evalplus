```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True  # initialize flag

    # Check for divisibility from 2 to string_length - 1
    for i in range(2, string_length - 1):
        if string_length % i == 0:
            is_prime = False
            break

    return is_prime
```

This function `is_prime_length()` takes an input string, calculates its length, and then checks if that length is prime by iterating through a range from 2 to _length - 1_ and checking for any divisors. Finally, it returns a boolean that signifies whether the length is a prime number or not. 

The function would be used alongside tests such as these to ensure that it operates correctly:
```python
# Testing the function
assert is_prime_length('Hello') == True
assert is_prime_length('abcdcba') == True
assert is_prime_length('kittens') == True
assert is_prime_length('orange') == False
```

This code uses the `assert` statement to check whether the `is_prime_length()` function returns the expected results for different test cases.