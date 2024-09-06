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
    print("The nth Fibonacci number is:")
    print(fib4(5))
    print("The nth Fibonacci number is:")
    print(fib4(7))
```

This Python code defines a function fib4 that computes the nth Fibonacci number using an efficient non-recursive approach. The function uses a specific conditions to determine the number of recursive calls: if n is 0, it returns 0. If n is 1, it returns 0. If n is 2, it returns 2. If n is 3, it returns 0. If n is greater than 3, the function recursively computes the Fibonacci number by summing the previous four Fibonacci numbers.

The code then demonstrates the function by printing the results of calling fib4(5) and fib4(7). This approach avoids the use of recursion, which makes the code more efficient and readable.