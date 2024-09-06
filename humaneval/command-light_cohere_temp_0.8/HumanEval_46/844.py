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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
This Python code defines a function called `fib4` that computes the nth element of the Fibonacci sequence using a loop-based approach. The `test_fib4` function is used to validate the `fib4` function's output for different input values. The `main` function, which is executed when the script is run, serves as the entry point, executing the `test_fib4` function to verify the correctness of the `fib4` function. 
This script is a complete self-contained implementation of the Fibonacci sequence computation, without reliance on external functions or modules.