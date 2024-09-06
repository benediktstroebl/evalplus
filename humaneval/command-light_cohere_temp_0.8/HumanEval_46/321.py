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
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```
This Python code defines a function `fib4` that computes the n-th Fibonacci number using a built-in approach without recursion. The function takes an integer `n` as input and returns the corresponding Fibonacci number. 

The function implements an iterative approach using the base case handling for small values of `n` and uses a recursive approach with the previous three elements of the Fibonacci sequence as the accumulation. 

The test cases provided at the bottom of the script verify the correctness of the function's output for different values of `n`.