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

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 1, returning `False` in such cases. If the number is 2 or 3, it returns `True`. Then, using a `while` loop, it checks for divisibility by numbers of the form `i` and `i + 2` where `i` is incremented by 6 at each step. If the number is divisible by any such number, `is_prime` returns `False`; otherwise, it returns `True`. 

The `prime_length` function then uses `is_prime` to check if the length of the provided string is a prime number, with the initial checks ensuring that string lengths of 2 or 3 are considered prime.

The logic employed allows the code to efficiently determine prime lengths, maintaining a reasonable runtime for longer strings.