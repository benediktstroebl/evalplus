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

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 3, returning True if so. If the number is greater than 3, it checks if it can be divided evenly by 2 or 3, returning False if so. Next, it begins iterating through a series of numbers, starting from 5. It checks if the given number is divisible by any of the numbers from 5 to the square root of the number, increasing by 6 each time. If the number is divisible by any of these, it returns False. If it reaches the end of the loop without finding a divisor, it returns True. 

The `prime_length` function takes a string and returns True if the length of the string is a prime number, and False otherwise. Inside the `prime_length` function, we first convert the string to a number to be able to use the `is_prime` function on it. We then call `is_prime` on the length of the string and if it returns True, we return True. Otherwise, we return False. 

This solution passes all the tests provided in the prompt and should be compatible with Python 3.