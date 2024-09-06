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
    # converting string to int to handle cases like '11' or '12345'
    length = int(len(string))
    return is_prime(length)
```

This approach takes advantage of the fact that the same primality test used for integers can be used to test the length of a string. 

The function `is_prime` implements the primality test: it checks if the number is less than or equal to 1, returns False; if the number is 2 or 3, returns True; if the number is divisible by 2 or 3, returns False; for larger numbers, it iterates through a series of numbers, starting from 2 and increasing by 6, and returns False if the number is divisible by any of them. If it finishes the iteration without finding a divisor, it returns True. 

The function `prime_length` uses the `is_prime` function to test the length of the string, which is converted to an integer for ease of use.

This solution passes the tests:
```
prime_length('Hello') == True
prime_length('abcdcba') == True
prime_length('kittens') == True
prime_length('orange') == False
``` 
and is justified as being correct.