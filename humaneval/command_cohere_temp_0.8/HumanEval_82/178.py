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
    if string <= 1:
        return False
    if is_prime(string):
        return True
    return False
```
This code first converts the input string into a number represented as a binary string, then checks if this number is prime. The `is_prime` function is an optimized primality testing function leveraging various shortcuts for common composite numbers. 

The above code is an optimized primality testing function, and the `prime_length` function is a straight-forward translation of the problem statement. It should also be noted that, in theory, the string-to-number-to-string process should be lossless, but this will cause issues for strings that include unmapped or out-of-range characters. This code does not account for those cases as it assumes the input is a string of ASCII characters.