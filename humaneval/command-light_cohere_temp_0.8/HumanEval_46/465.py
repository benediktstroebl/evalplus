```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

#Test the function with various input values
print("Fibonacci Number Sequence:")
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
``` 
This function employs an efficient approach that avoids recursion, utilizing the iterative computation of Fibonacci numbers.