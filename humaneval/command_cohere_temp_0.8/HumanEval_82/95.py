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
    # Using a generator to calculate the length of a string
    yield from str_length = (len(string) for string in string if string != '0')
    return is_prime(str_length)
```
This code first generates the length of the string but avoids converting the entire string to a number to conserve memory and still generate the length. It then uses the is_prime function to determine if the generated length is prime. 
The is_prime function is an optimized version of the bottleneck of most prime checking functions, the checking of successive primes. It checks for divisibility by 2 and 3 at the start since these are the most frequent primes. It then checks in steps of 6 since these numbers cover the remaining prime numbers. For example, 5, 11, 17, 23, 29 are the successive primes it doesn't check as they can be expressed as 6k ± 1, 6k ± 2, 6k ± 3, 6k ± 4, 6k ± 5.

The previous code minimizes the number of divisions and comparisons needed to determine if a number is prime.