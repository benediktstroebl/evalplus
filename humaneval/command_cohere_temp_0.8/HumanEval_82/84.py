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

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 3, returning True if so. If the number is greater than 3, it checks if it's even or divisible by 3, and returns False if so. Using the outer loop iteration variable i (initially set to 5), it iterates through numbers 5, 7, 11, 13, 17, 19, and so on, progressively testing whether the number is divisible by 2, 3, 5, 7, 11, 13, 17, 19, and so on, ultimately arriving at the square root of the number. If the number is divisible by any adjacent pair of numbers during this iteration, it returns False. Otherwise, it returns True, indicating that the number is prime.

The `prime_length` function then uses `is_prime` to check if the length of the provided string is prime. It first casts the string to a number using len(string) and then checks if it's prime, as explained above.

This solution achieves the intended functionality, accurately determining if the length of a string is a prime number.