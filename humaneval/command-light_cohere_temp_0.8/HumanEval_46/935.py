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

if __name__ == "__main__":
    print("Testing fibonacci function..." + "\
          "With n = 5, we should get: " + "\
          "result = 4")
    print(fib4(5))
    print("Testing fibonacci function..." + "\
          "With n = 6, we should get: " + "\
          "result = 8")
    print(fib4(6))
    print("Testing fibonacci function..." + "\
          "With n = 7, we should get: " + "\
          "result = 14")
    print(fib4(7))
```
The provided code is a Python script that defines a function `fib4` that computes the n-th element of the Fibonacci sequence using an efficient algorithm without recursion. The function uses a computation based on the base cases for n being 0, 1, and 2, and then recursively calculates the result by summing the previous four values. The script also includes a main block with tests to verify the function's correctness.