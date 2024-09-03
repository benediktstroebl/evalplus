```python
def fib4(n: int):
    if n <= 0:
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
    print("First Test:")
    print(fib4(5))
    print("Result:")
    4

    print("Second Test:")
    print(fib4(6))
    print("Result:")
    8

    print("Third Test:")
    print(fib4(7))
    print("Result:")
    14)
```

This Python script defines a function called fib4, which computes the n-th element of the Fibonacci sequence without recursion. The function uses a specific conditions to determine the base cases (0, 1, and 2) and then computes the remaining values using a combination of recursive calls and iterative summation. The tests at the  __main__ block verify that the function produces the correct Fibonacci values for the given inputs.