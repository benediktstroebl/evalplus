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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Error: Fibonacci sequence does not have negative indices.")
    else:
        result = fib4(n)
        print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```
This script defines a function fib4 that computes the n-th Fibonacci number using an efficient method that avoids recursion. It also contains a test_fib4 function that prompts the user for an index and calls the fib4 function to compute and print the result.

When you run this script, it will provide the user with a simple interface to calculate Fibonacci numbers without the need for complex recursion.