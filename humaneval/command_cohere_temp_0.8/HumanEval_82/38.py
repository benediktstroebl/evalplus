```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True
    
    # Check if the length is divisible by any number from 2 to the square root of length
    for i in range(2, int(string_length**0.5) + 1):
        if string_length % i == 0:
            is_prime = False
            break

    return is_prime

# Test cases
print(is_prime_length('Hello'))  # Output: True
print(is_prime_length('abcdcba'))  # Output: True
print(is_prime_length('kittens'))  # Output: True
print(is_prime_length('orange'))  # Output: False
```

In the Python script above, the `is_prime_length` function takes an input string and determines whether its length is prime. The function initially assumes the length is prime and sets `is_prime` to True. It then checks if the length is divisible by any number from 2 to the square root of the length. If a divisor is found, the `is_prime` variable is set to False, indicating a non-prime length. The function returns the value of `is_prime` as the result.

Each test case is executed within the script to verify the correctness of the `is_prime_length` function. The output statements print the results of each test case, ensuring that the function appropriately identifies prime and non-prime string lengths.