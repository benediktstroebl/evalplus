```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.
    See https https: https://en.math.math.2/fibonacci.com/library/com.math/algorithm/thepy
    main
    """
    # helper function to check if a number is prime
    def is_prime(num: int):
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
    # generate the nth Fibonacci number and check if it's prime
    fib_num = fibonacci(n)
    if is_prime(fib_num):
        return True
    else:
        return False
    # helper function to generate the nth Fibonacci number
    def fibonacci(num: int):
        if num == 0:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

# test the function
print(prime_fib(5))

``` 
This code defines a function `prime_fib` that calculates the nth Fibonacci number and checks if it is prime. The function also includes a helper function `is_prime` to check if a given number is prime, and a helper function `fibonacci` to generate the nth Fibonacci number recursively.