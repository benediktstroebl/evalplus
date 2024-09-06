```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True 

    for i in range(2, int(string_length**0.5) + 1):
        if string_length % i == 0:
            is_prime = False
            break
    
    return is_prime
```

This function `is_prime_length` takes a string as an input and returns True if the length of the string is a prime number or False otherwise. It checks if the string length can be divided by any number from 2 to the square root of the string length. If there is any divisor, it returns False, if not, it returns True. 

The function is self-contained and can be copied and run as is to test it against some examples. 

In order to test it against the provided examples, you can run the following:
```python
print(is_prime_length('Hello'))  # Should print True
print(is_prime_length('abcdcba'))  # Should print True
print(is_prime_length('kittens'))  # Should print True
print(is_prime_length('orange'))  # Should print False
```

This will test the function against the provided examples from the prompt. 

Note that the function may not be the most efficient one to tackle this problem as it tries to check for divisors up to `int(string_length**0.5)`. However, it is a straightforward and manageable approach for pulling off this task.  If chasing optimum performance, you might want to consider more sophisticated algorithms like the `Sieve of Eratosthenes` for checking prime lengths.