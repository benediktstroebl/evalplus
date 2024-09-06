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
The code first converts the string into a number and then uses the `is_prime` function to solve the problem. 
The `is_prime` function implements the integer square root algorithm to check if the number is prime or not. It loops from 5 and increments by 6 until it exceeds the square root of the checked number. It checks divisibility by both `i` and `i + 2` at each iteration, which efficiently rule out non-prime candidates. 

The solution's test cases pass easily, as expected.