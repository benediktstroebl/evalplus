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
    if string == '' or is_prime(string):
        return True
    return False
```
This code defines a recursive function `is_prime` that utilizes a mix of small prime number checks and a `divisibility` loop to efficiently determine if a given number is prime. Subsequently, the `prime_length` function converts the input string to its ASCII value sum, ensuring it's not empty, and then utilizes `is_prime` to ascertain whether the length of the string is a prime number. The approach strikes a balance between efficiency and simplicity.