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
    assert fib4(n) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
``` 
This code defines a function `fib4` that computes the n-th element of the Fibonacci sequence using the recursive definition. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The code also includes a test function `test_fib4` that verifies the correctness of the `fib4` function by checking if the result of `fib4` is equal to `14` for `n = 7`. This test passes and demonstrates that the function correctly computes the n-th Fibonacci number in the given range.