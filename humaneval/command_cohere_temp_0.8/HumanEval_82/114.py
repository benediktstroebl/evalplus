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

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 3, returning True if so. If the number is greater than 3, it checks if it's even or divides by 3, then it returns False. It then starts checking for divisors from 5 onwards, incrementing by 6 each time to narrow down potential divisors. 

The `prime_length` function then uses this `is_prime` function to check if the length of the input string is prime.

The test cases provided in the prompt assume various successful and unsuccessful strings to test the `prime_length` function. 

This code should be robust and efficient enough to handle various scenarios successfully.  If there are any questions or concerns about the code, feel free to ask!