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
    # converting the sum to string to make it a valid input for is_prime
    return is_prime(int(string))
```
This code defines a function 'prime_length' that takes a string and converts it to a prime number or not, it then converts the string to a sum of ASCII values and converts that sum to an integer to be checked for primality using the 'is_prime' function. 

The 'is_prime' function implements a primality testing algorithm called the '6k ± 1 rule', it checks if a number is prime or not by iteratively checking divisibility by numbers of the form 6k ± 1, starting from 5 (since any non-prime number has at least one factor that is 1, 2, 3, or 5). It returns True if the number is prime or False otherwise.

The code addresses the problem statement and gives a correct answer to the prompt, as it returns True for strings that represent prime numbers in ASCII and False otherwise.