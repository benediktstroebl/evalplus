```python
def fib4(n: int):
    """The Fibonacci sequence, as a Python function. The function takes an integer n as input and returns the n-th Fibonacci number.
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
    """Function to test the fib4 function.
    n = int(input("Enter the value of n: "))
    if n < 0:
        print("Error: n must be a positive integer.")
    else:
        result = fib4(n)
        print(f"The {n}-th Fibonacci number is: {result}")

test_fib4()
```

This code defines a Fibonacci sequence generator function that uses the Fibonacci sequence formula. The function calculates each number in the sequence using recursion and then returns the result. The code also includes a test function that prompts the user to enter a value for 'n', and then calls the `fib4` function to calculate and print the result.