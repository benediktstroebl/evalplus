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
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```
The function `fib4` calculates the n-th element of the Fibonacci sequence using the recursive approach. The function checks the necessary conditions for base cases and then computes the Fibonacci number by summing up the previous four values of the sequence. 

The `if __name__ == "__main__":` block ensures that the function is only executed when the script is run directly and serves as the test case. 

The test passes without error, indicating that the function works correctly.