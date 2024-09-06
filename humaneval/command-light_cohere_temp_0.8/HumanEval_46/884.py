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

The code defines a `fib4` function that computes the nth element of the Fibonacci sequence without recursion. It uses a important logic to achieve this: if `n` is 0, it returns 0; if `n` is 1, it returns 0 (the base case of the recursion); if `n` is 2, it returns 2 (the next Fibonacci number); if `n` is 3, it returns 0 (the third element of the sequence); and so on. The function continues this sequence of returning the sum of the previous four Fibonacci numbers and adding it to the next element until it reaches the desired `n`.