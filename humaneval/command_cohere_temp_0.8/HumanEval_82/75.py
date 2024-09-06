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
    return is_prime(len(string))
```

The `is_prime` function checks whether a given number is prime. It first handles special cases for numbers less than or equal to 3, then uses a mix of checks and trial division to determine whether the number is prime. The `prime_length` function iterates over each character in the string, converting the string length to a number and then checking if it's prime using the `is_prime` function. 

The test cases provided in the prompt assume both functions are already defined and correctly implemented, therefore the functions must be defined in the correct scope for the tests to work, this can be seen in the following example:
```python
# The tests will fail unless the functions are defined in the correct scope
def is_prime(number):
    # ...

def prime_length(string):
    # ...
``` 

In this way, the `prime_length` function can call the `is_prime` function correctly. 
The code neatly solves the problem in a self-contained manner, providing a clear function to check for prime string lengths.