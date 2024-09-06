```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which the first two are 0 and 1 and each subsequent number is the sum of the preceding two.
    """
    numbers in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    """
    print("Testing the Fibonacci function...")
    test_fib4()

if __name__ == "__main__":
    main()
```
The code defines a function `fib4` which computes the n-th Fibonacci number using the iterative approach. The function starts with the basic case of n=0, which returns 0. Then, it checks for other special cases of n=1, 2, and 3. After that, it recursively calls the `fib4` function with `(n-1)` and `(n-2)` to compute the Fibonacci numbers. The recursive calls are added together with the previous two Fibonacci numbers to get the result for `n`. 

The `test_fib4` function then tests the `fib4` function with different values of `n` and checks that the results are correct. The `main` function is called at the end, and it prints a message that starts the testing process.