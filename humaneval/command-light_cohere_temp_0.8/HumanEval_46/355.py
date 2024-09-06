```python
def fib4(n: int):
    """The Fibonacci sequence 4 numbers formula:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    for i in range(0, 7):
        print(fib4(i), end=" ")
    print()
```
The code defines a Python function `fib4` that computes the n-th element of the Fibonacci sequence using the formula for the 4 numbers sequence. The function returns 0 if n is 0, 1, or 2, and uses the recursive Fibonacci sequence formula for other cases. The `main` block then iterates through the range of 0 to 7, and for each value of n, it calls the `fib4` function and prints the result. 
This code is a complete, self-contained solution to the problem.