```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and a boolean indicating whether it's prime.

    Returns either the Accomplished Fibonacci number or infinity if it's not a prime.
    """
    returns the value of nth Fibonacci number and True.
    """
    return (next(n) ** 2, is_prime(next(n) * next(n) + 1)))

def is_prime(n: int):
    """
    Tests whether number n is prime.

    Returns True if n is a prime and False otherwise.
    """
    checks the if n is less than 1 or is divisible by any integer with a prime factor greater than or equal to sqrt(n).
    """
    return n <= 1 or any_of(n == 2 or n == divisors(n))

def main():
    """
    Test the prime_fib function

    n = int(input("Enter a number: "))

    if n < 1:
        print("Error: Please enter a positive integer.")
    else:
        result, is_prime = prime_fib(n)
        print(f"The {n}-th Fibonacci number and whether it's prime:")
        print(f"{result} ({is_prime})")

if __name__ == "__main__":
    main()
```

This code defines a function `prime_fib` that returns the nth Fibonacci number and a boolean indicating whether it is prime. Additionally, it defines a function `is_prime` to test whether a given number is prime or not. The `main` function is the driver of this script, and it takes user input to solve the problem.