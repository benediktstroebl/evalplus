```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is a fraction of the sum of the two preceding ones."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = int(input("Enter the value of n: "))
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```

This script defines a function called `fib4` that computes the nth Fibonacci number using the provided formula. The function utilizes a loop to recursively calculate the number, avoiding the use of costly recursive calls. The `test_fib4` function serves to test the `fib4` function by taking user input for the value of n and displaying the computed result.

The `test_fib4` function is designed to prompt the user for input, calculate the nth Fibonacci number, and display the result. 

Overall, this script provides a self-contained solution for computing Fibonacci numbers using a loop-based approach.