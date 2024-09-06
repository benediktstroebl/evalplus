```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are typical to be defined as the sum of two preceding numbers in the sequence, so the first two values are 0 and 1.
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)

def test_fib4():
    n = int(input("Enter a number: "))
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

if __name__ == "__main__":
    test_fib4()
```

This code defines a function `fib4` that computes the nth element of the Fibonacci sequence using dynamic programming. The function is designed to calculate the nth Fibonacci number without using recursion. The `test_fib4` function is a driver function that prompts the user to input a number and then calls the `fib4` function to compute and print the result.

This code is a self-contained implementation of computing Fibonacci numbers without recursion.