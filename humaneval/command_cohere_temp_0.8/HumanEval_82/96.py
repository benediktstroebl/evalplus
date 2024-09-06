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
    if len(string) == 2:
        return True
    if len(string) % 2 == 0:
        return False
    for char in string:
        if is_prime(ord(char)):
            continue 
        else:
            return False
    return True
```

The `is_prime` function checks if a given number is prime using the trial division method optimized for performance. It checks if the number is less than or equal to 3, then it is prime. If the number is greater than 3, it checks if it can be divided by 2 or 3, if so, it is not prime. From there, it iterates through numbers of the form 6k ± 1 (skipping odd numbers), starting from 5 until it reaches the square root of the number. If the number is divisible by any number in this range, it is not prime. If it isn't, it is prime.

The `prime_length` function first handles edge cases where the length of the string is less than or equal to 1, returning False, and if the length is 2, it returns True. If the length is even, it also returns False. Finally, it loops through each character in the string and checks if the Unicode value of each character is prime. If it is, it continues to the next character, if not, it returns False. If it reaches the end of the loop, the function returns True.