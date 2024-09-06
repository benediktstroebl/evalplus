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

# Test Cases
print(is_prime_length('Hello'))  # Output: True
print(is_prime_length('abcdcba'))  # Output: True
print(is_prime_length('kittens'))  # Output: True
print(is_prime_length('orange'))  # Output: False
```

The above `is_prime_length` function takes an input string, calculates its length, and then checks if this length is prime by iterating from 2 up to the square root of the length (a well-known optimization). The function returns True if the length is prime and False otherwise.