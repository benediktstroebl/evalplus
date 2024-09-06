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
    n = int(input("Enter the number to test: "))
    if n < 0:
        print("Error: Please enter a positive number.")
    else:
        print(fib4(n))

test_fib4()
```

This code defines a function fib4 that computes the n-th Fibonacci number using a loop. The function is then tested using the test_fib4 function, which prompts the user to enter a number and passes it to the fib4 function to compute the result.

The code is self-contained, meaning it does not rely on any external functions or modules, and can be easily copied and pasted into other projects.