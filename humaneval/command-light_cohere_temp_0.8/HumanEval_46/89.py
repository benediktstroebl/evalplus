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
This script provides a function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using a loop-free approach. The function returns 0 for base cases (n==0,1) and uses the `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)` to compute the n-th Fibonacci number in the sequence. 

The function is then tested by calling `fib4` with different values of `n` and printing the results.

Now, you can call this function with any input value of `n` to get the corresponding Fibonacci number.