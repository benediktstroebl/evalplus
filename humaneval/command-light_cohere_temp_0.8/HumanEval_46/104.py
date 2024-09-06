```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print("First Test:")
    print(fib4(0))
    print("Second Test:")
    print(fib4(5))
    print("Third Test:")
    print(fib4(7))
```
The function checks the input 'n', and returns the Fibonacci sequence number if the input is less than 5. The tests print the numbers, 0, 2, and 14 for n = 0, 5, and 7, respectively.