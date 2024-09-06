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
    # Convert string to an integer and then check its primality
    if is_prime(len(string)):
        return True
    return False
```

The `is_prime` function uses a mix of small prime number checks and a loop to determine whether an integer is prime. Afterward, the `prime_length` function converts the string's length into an integer and uses `is_prime` to determine if it's prime. 

The example tests provided in the prompt will return `True` for strings like 'Hello', 'abcdcba', and 'kittens', and `False` for strings like 'orange'. 

Let me know if you'd like me to explain any part of the code in further detail.