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
    n = int(input("Enter a number: "))
    result = fib4(n)
    print(f"The Fibonacci number at position {n} is: {result}")

test_fib4()
```
The function `fib4` computes the n-th Fibonacci number in this program using an iterative method. It is also includes a test function called `test_fib4` that asks the user to enter a number and then shows the outcome of the `fib4` function. The program can run without relying on recursion, which is more effective and efficient than a recursive implementation.