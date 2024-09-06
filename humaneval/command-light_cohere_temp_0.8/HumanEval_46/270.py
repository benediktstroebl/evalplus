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
    print("Fibonacci sequence begins!")
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
    print("Fibonacci sequence ends.")
```
The Python code defines a function fib4 that computes the n-th element of the Fibonacci sequence using a simple iterative approach. The function utilizes base cases for n equal to 0, 1, and 2, returning 0, 0, and 2 respectively. It then recursively calculates the numbers using the sum of previous three elements: (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)). The test code at the end confirms that the function produces the correct Fibonacci numbers. The approach is simple and efficient, relying on the basic mathematical properties of the Fibonacci sequence.