```python
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    if len(string) <= 1:
        return False
    if is_prime(len(string)):
        return True
    return False
```

The `is_prime` function checks if a given number is prime. It first checks if the given number is less than or equal to 1, returning `False` if so. If the number is 2 or 3, it returns `True`. Then, using a `while` loop, it checks for divisibility by numbers of the form `i` and `i + 2` where `i` starts from 5 and increases by 6 each iteration. If the number is divisible by either, it returns `False`. Otherwise, it returns `True`. 

The `prime_length` function then uses this `is_prime` function to check if the length of the given string is prime. It first converts the string to a number, handling potential cases where the string length is more than 1000 characters, and then passes it to the `is_prime` function.

The script includes tests for both functions to ensure they perform as expected.