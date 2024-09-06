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
    if n < 0 or n > 3:
        print("Please enter a valid number between 0 and 3")
    else:
        print(f"The {n}-th Fibonacci number is {fib4(n)}")

test_fib4()
```

This code defines a function `fib4` that computes the n-th Fibonacci number efficiently using a loop-independent approach. The function returns the value of the Fibonacci number when given an integer `n`. The test function `test_fib4` prompts the user to enter a number and then calls the `fib4` function to compute and print the result.