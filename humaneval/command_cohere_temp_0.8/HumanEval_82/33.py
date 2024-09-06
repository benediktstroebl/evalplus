```python
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
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

The function `prime_length` calculates the ASCII value sum of the characters in the input string using the sum and `map` functions and then converts it to an integer for prime checking. The `is_prime` function checks if the length is prime using an optimized trial division method. It returns True if the length is prime and False otherwise.