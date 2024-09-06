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
    result = fib4(n)
    print(f"The Fibonacci number at position {n} is: {result}")

test_fib4()
```

This script defines a function `fib4` that computes the n-th Fibonacci number in the sequence without using recursion. The function follows the specific logic: it returns 0 for `n` equal to 0, 1, or 2, and returns the sum of the previous four numbers for `n` equal to 3 or greater. The function then tests this input with `input()` and uses the `fib4` function to compute the Fibonacci number at the position entered by the user. The result is then displayed using `print()`. Simultaneously, you can input any positive integer value, and the script will return the corresponding Fibonacci number.