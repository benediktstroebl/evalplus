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

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```
This Python code defines a function fib4 that computes the n-th value of the Fibonacci sequence using a formula-based approach. It uses a specific to the Fibonacci sequence, which is a series of numbers where each successive number is the sum of the two preceding ones. 

The function uses a series of conditional statements to determine the value of the n-th Fibonacci number based on the values of earlier numbers. The final value is returned by the function.

The code also has a main block where the function is called with various input values (5, 6, 7) and the results are printed. The output will display the corresponding Fibonacci numbers.