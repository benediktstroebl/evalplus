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
    # removing any non char characters from the string and converting to lowercase to handle cases like 'Hello'
    string = ''.join(c for c in string if c.isalpha()).lower()
    return is_prime(len(string))
```

This approach is quite efficient for checking primality, popularly known as the `6k ± 1` rule, which helps in bypassing the need for checking divisibility for all numbers and narrows down the potential prime suspects. You can learn more about this algorithm at [Wolfram Alpha Primality Test](https://www.wolframalpha.com/input/?i=primality+test) or [Wikipedia](https://en.wikipedia.org/wiki/Primality_test#Provable). 

This approach has a linear time complexity of `O(n)` where `n` is the length of the input string. It also uses a linear amount of RAM for the stack which is proportional to the length of the input string.