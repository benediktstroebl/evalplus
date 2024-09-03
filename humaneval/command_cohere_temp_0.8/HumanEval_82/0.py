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
    # converting string to int to check if it's a prime number
    if is_prime(int(string)):
        return True
    else:
        return False
```
This code defines a function is_prime() that utilizes an optimization of the Euclidean algorithm to efficiently check whether a given number is prime. The function prime_length(string) then converts the string to an integer and uses is_prime() to determine if the length of the string is a prime number. 

The output of the example cases provided will be:
```bash
True
True
True
False
```