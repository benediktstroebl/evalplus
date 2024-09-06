```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        prime1 = 2
        prime2 = 3
        for i in range(5, n+1, 6):
            prime1, prime2 = prime2, prime1 + prime1
            if is_prime(prime1):
                break
        return prime2

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib_test():
    n = int(input("Enter n: "))
    result = prime_fib(n)
    print(f"The {n}th Fibonacci number is: {result}")

# Test user input
prime_fib_test()
``` 
The provided code defines a function `prime_fib` that calculates the n-th Fibonacci number, which is a prime, and another function `is_prime` that checks whether a given number is prime or not. The code also includes a test function `prime_fib_test` that prompts the user to input a number and passes it to the `prime_fib` function to calculate the result. 
This script can be used to find the n-th Fibonacci number, which is a prime, and it can also test the correctness of the function.