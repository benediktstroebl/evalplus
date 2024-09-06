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
    n = 7
    assert fib4(n) == 14  # True

def main():
    test_fib4()

if __name__ == "__main__":
    main()
``` 
The provided code defines a Python function called fib4 that computes the n-th element of the Fibonacci sequence using a technique that avoids recursion. The function uses a combination of if-else statements and a recursive approach to calculate the Fibonacci number. 

The test_fib4 function is responsible for testing the fib4 function by calling it with a specific value for n and asserting that the result is correct. The main function is the entry point for the program and calls the test_fib4 function to run the tests.