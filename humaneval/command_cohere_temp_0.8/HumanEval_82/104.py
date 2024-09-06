```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True

    if string_length < 2:
        return False

    for i in range(2, int(string_length**0.5) + 1):
        if string_length % i == 0:
            is_prime = False
            break

    return is_prime

# Test Suite
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return is_prime_length(string)

# Example Usage
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
```

This script defines a function `is_prime_length()` that checks whether the length of the input string is a prime number. It iterates through numbers from 2 up to the square root of the string length, checking for divisibility. 

The `prime_length()` function is included as the example usage in the Markdown code block, but it is not necessary as the underlying function is_prime_length() already encapsulates the logic of prime length. 

The script returns True for the examples 'Hello', 'abcdcba', and 'kittens', and False for the example 'orange'. 
To test the function, uncomment the example usage line and comment out the `print` statements to execute the function with these examples.  This will help verify its behavior against the expected outputs.  Any other string can also be used for additional testing.