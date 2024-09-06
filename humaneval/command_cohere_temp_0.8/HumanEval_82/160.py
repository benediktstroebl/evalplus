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
This code defines a recursive function `is_prime` that checks whether a given number is prime or not. It then calls this function on the length of a given string to determine if the length is prime. 
The `prime_length` function takes a string and returns True if the string's length is a prime number or False otherwise. It passes the test cases provided, as it returns True for strings with prime lengths and False for strings with non-prime lengths.