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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

if __name__ == "__main__":
    print("The Fibonacci sequence is:")
    print(fib4(5))
    print("The n-th element of the Fibonacci sequence is:")
    print(fib4(7))
```
The above Python script defines a function fib4 that computes the n-th element of the Fibonacci sequence using a formula-based approach. It uses a value of n to check which Fibonacci number needs to be computed, and then returns the calculated Fibonacci number. The script also contains a main function, which tests the fib4 function with different values of n and prints the results.