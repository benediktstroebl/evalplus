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
    print("Testing the Fibonacci sequence function...")
    print("Result for n = 5:", fib4(5))  # Output: 4
    print("Result for n = 6:", fib4(6))  # Output: 8
    print("Result for n = 7:", fib4(7))  # Output: 14
```

This Python script defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a recursive approach without recursion. It employs a specific logic to calculate each number in the sequence, adhering to the standard definition. The function is then tested and demonstrated with test cases for different values of n.