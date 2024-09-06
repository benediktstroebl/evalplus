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
    string = str(sum(map(ord, string)))
    if string == '' or is_prime(string):
        return True
    return False
```

The function `prime_length` calculates the sum of ASCII values of characters in the input string and then checks whether this sum is either empty or a prime number. The `is_prime` function is used to determine whether a given integer is prime. This function checks whether the number is less than or equal to 3, then checks if the number is divisible by 2 or 3, and then uses a loop to check divisibility by numbers of the form `i` and `i + 2`, where `i` starts from 5. If no divisors are found after the loop, the number is prime.