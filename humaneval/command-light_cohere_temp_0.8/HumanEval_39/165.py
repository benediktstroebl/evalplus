```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0:
        return 3
    else:
        def helper(num):
            if num <= 1:
                return num
            elif num <= 3:
                return 5
            elif num % 2 == 0:
                return 13
            else:
                return helper(num - 1) + 2
        return helper(n)

print(prime_fib(5))
``` 
This function, `prime_fib`, takes an integer `n` as input and returns the n-th Fibonacci number that is also prime. It uses a recursive and iterative approaches to achieve this.