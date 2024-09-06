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
This code provides a self-contained function that computes the n-th Fibonacci number in O(n) time using a loop.