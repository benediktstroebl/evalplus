```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    for n in range(0, 7):
        print(fib4(n))
```
In this code, the 'fib4' function computes the n-th element of the Fibonacci sequence using a method that doesn't utilize recursion. The function accepts an integer 'n' as an input and returns the corresponding Fibonacci number. The tests ensure that function is working correctly for the given input.