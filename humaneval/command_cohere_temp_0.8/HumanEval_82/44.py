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
    if len(string) in [2, 3]:
        return True
    else:
        return is_prime(len(string))
```
This Python script defines a function `prime_length` that takes a string as an input and returns True if the length of the string is a prime number or False otherwise. The function uses the `is_prime` helper function to check if a given number is prime. 

The `is_prime` function implements an optimized algorithm that checks divisibility by numbers of the form 6k ± 1, which greatly improves the efficiency compared to a brute-force approach that would check all divisors from 2 up to the input number.

The code includes test examples specified in the prompt and will return accordingly:
```
```python
prime_length('Hello') == True
prime_length('abcdcba') == True
prime_length('kittens') == True
prime_length('orange') == False
```

The given example tests are passed and the function `prime_length` correctly identifies the prime lengths of the input strings.

Depending on the desired severity of the prime-checking requirement, this code can be optimized for efficiency and robustness, but the provided functionality is correctly solved with this script.