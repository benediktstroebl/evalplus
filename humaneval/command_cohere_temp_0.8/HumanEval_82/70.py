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

The function `prime_length` takes a string and returns True if the length of the string is a prime number or False otherwise. To accomplish this, the nested function `is_prime` is used to determine whether a given number is prime or not. This function uses a combination of small prime numbers and divisibility checks to quickly rule out non-prime candidates.

The `prime_length` function first converts the input string to a integer to make the prime checking easier. It then checks if the length is less than or equal to 1 which would make it false. It then passes the length to the `is_prime` function to check if the length is prime or not. 

This solution adheres to the problem guidelines and provides an accurate prime checking mechanism.