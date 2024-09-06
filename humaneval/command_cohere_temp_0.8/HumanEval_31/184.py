Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function returns true if the given number is prime, and false otherwise. It checks if the given number is less than 2, and if so, it returns false. It then iterates from 2 up to the square root of the given number, and for each number in that range, it checks if the given number is divisible by it. If it is, then the number is not prime, and the function returns false. If the loop completes without a divisor being found, then the number is prime, and the function returns true. 

This solution corresponds to the provided example tests, and it should generally be quite efficient for determining whether a number is prime or not. 

Here is how you could use this function in another Python script:
```python
number = 61
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
``` 
This should output "61 is a prime number." if the script is run in the expected context. If you have any other questions, feel free to ask!