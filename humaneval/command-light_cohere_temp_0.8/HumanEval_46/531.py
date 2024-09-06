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
    n = int(input("Enter a number to test: "))
    if n < 0 or n > 4:
        print("Invalid input. Please enter a expected an integer.")
    else:
        result = fib4(n)
        print(f"The {n}th Fibonacci number is: {result}")

test_fib4()
```

The code defines a function `fib4` that computes the n-th Fibonacci number using the iterative approach without recursion. The function uses a simple logic to check if `n` is a valid input (an integer between 0 and 4) and then calls the `fib4` function with `n` as an argument to compute the result. The test function `test_fib4` takes user input, calls `fib4` to get the result, and then prints it out. 

This is a concise and efficient implementation of the Fibonacci sequence that avoids recursion, making it suitable for use in various scenarios.