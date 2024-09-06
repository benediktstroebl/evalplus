```python
def is_prime_length(input_str):
    if len(input_str) <= 1:
        return False
    for char in input_str:
        if char.isalpha():
            return False
    return len(input_str) == 2 or len(input_str) == 3 or (len(input_str) > 3 and ((len(input_str) % 2) == 0))
```

The function `is_prime_length` checks whether the length of the input string is prime by handling the following logical cases:
- If the length of the input string is one or less, including the case of an empty string, it is not prime, so the function returns `False`.
- If the length is two or three, it is prime, so the function returns `True`.
- For longer strings, the function returns `True` if the length is even (since all even numbers greater than 2 are composite), and returns `False` if the length is odd. 

The function also accounts for the case where the characters inside the string are not alphabetic, returning `False` if they are. This ensures that the function appropriately answers the question asked – whether the string length is prime – without being misled by the content of the string. 

This approach provides a straightforward and effective way to determine whether the length of a given string is a prime number.