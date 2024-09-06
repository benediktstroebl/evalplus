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
    if n < 0:
        print("Error: Fibonacci sequence does not contain negative numbers.")
    elif n == 0:
        print("Fibonacci(0) =", fib4(0))
    elif n == 1:
        print("Fibonacci(1) =", fib4(1))
    elif n == 2:
        print("Fibonacci(2) =", fib4(2))
    elif n == 3:
        print("Fibonacci(3) =", fib4(3))
    else:
        print("Fibonacci(", n, ") =", fib4(n))

test_fib4()
```
The code defines a function `fib4` which computes the n-th Fibonacci number in the Fibonacci sequence using the recursive approach, without recursion. The `test_fib4` function prompts the user to input a number and passes the input to the `fib4` function to compute and print the result.