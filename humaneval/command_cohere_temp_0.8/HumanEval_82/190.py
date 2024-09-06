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
    string = str(sum(map(ord, string)))
    if string == '0' or string == '1':
        return False
    return is_prime(string)
```
This code defines a recursive function `is_prime` that utilizes a mix of small prime number checks and a `divisibility` loop to efficiently determine if an input number is prime or not. It then uses this function to check if the length of the input string, converted to an integer, is prime. The function 'prime_length' first converts the string to its sum of ASCII values, assuming that the input string is ASCII. Subsequently, it converts this sum to an integer to facilitate the primality check. Two special cases, '0' and '1', are excluded from consideration as they have distinct behavioral properties.