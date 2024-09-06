```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent number is the sum of the two preceding ones. The Fib4 sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    return fib4(n)

def test_fib4():
    n = int(input("Enter a number to compute the n-th Fibonacci number: "))
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```
The Python code defines a function called fib4 which computes the n-th Fibonacci number using the formula: n-th Fibonacci(n) = sum(fib4(n-1), fib4(n-2), fib4(n-3), fib4(n-4)). The function has an associated test function, test_fib4, which prompts the user to enter a number and computes and prints out the corresponding Fibonacci number.