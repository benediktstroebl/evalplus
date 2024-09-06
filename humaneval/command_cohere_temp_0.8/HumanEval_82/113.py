```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True
    
    # Check if the length is divisible by any number from 2 to the square root of the length
    for i in range(2, int(string_length**0.5) + 1):
        if string_length % i == 0:
            is_prime = False
            break
    
    return is_prime

# Test Cases
print(is_prime_length('Hello'))  # Output: True
print(is_prime_length('abcdcba'))  # Output: True
print(is_prime_length('kittens'))  # Output: True
print(is_prime_length('orange'))  # Output: False
```

The function `is_prime_length` checks if the length of the input string is prime. It begins by assigning the length of the input string to the variable `string_length`. It initially assumes that the length is prime and sets `is_prime` to True. The function then checks if the length is divisible by any number from 2 to the square root of the length. If a divisor is found, the `is_prime` variable is set to False, indicating that the length is not prime. If no divisor is found, the function returns True, indicating that the length is prime.

The output of the test cases provided is True for the three qualifying strings and False for 'orange'.