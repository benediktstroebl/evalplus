```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
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
    n = int(input("Enter a number to test: "))
    result = fib4(n)
    print(f"The Fibonacci number at index {n} is {result}")

test_fib4()
```

This script defines a function `fib4` that computes the n-th Fibonacci number in a loop using the iterative approach. The function first checks the basic cases: if n is 0 or 1, it returns 0. Then, it checks for the cases where it can directly return the result using the base cases. 

The `test_fib4` function prompts the user for a number and passes it to the `fib4` function to compute and print the Fibonacci number at the corresponding index.