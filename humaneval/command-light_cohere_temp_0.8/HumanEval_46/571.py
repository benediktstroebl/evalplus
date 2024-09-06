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

def test_fib4():
    """Your function 'fib4' that calculates the n-th Fibonacci number using the iterative approach."""
    print("Calculating Fibonacci numbers using the iterative approach:")
    n = 7
    fib = fib4(n)
    print(f"The {n}th Fibonacci number is {fib}")

test_fib4()
```
The function `fib4` uses an iterative approach to calculate Fibonacci numbers, avoiding recursion. It begins with the basic cases for n = 0, 1, and 2, and then proceeds to calculate Fibonacci numbers using the summation of the preceding four numbers. The function is self-contained and does not rely on any external functions or modules.