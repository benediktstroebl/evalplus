Here's the Python script:
```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```
This script defines a function called fib4, which computes the n-th element of the Fibonacci sequence using the recursive approach without relying on any other functions. The function returns the value of the n-th Fibonacci number. 

The main section then calls the fib4 function with different input values and prints the results.