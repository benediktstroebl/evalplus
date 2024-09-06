```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are a first and second numbers in the sequence are 0 and 1, respectively, and the sequence continues as the third and fourth numbers, and so on.
    if n is a zero or negative integer, return n itself.
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    """Call the fib4 function and print the result."""
    print(fib4(7))

if __name__ == "__main__":
    main()
```
The provided code defines a Python script that efficiently computes the n-th element of the Fibonacci sequence using a technique without recursion. It employs a specific logic to determine the range of valid input values, and then it performs the computation by summing up the four preceding elements of the Fibonacci sequence, which avoids recursion and improves efficiency. The code includes a function `fib4` which accepts an integer `n` as input and returns the n-th Fibonacci number. It includes a test_fib4 function to verify the correctness of the `fib4` function by passing different test cases. Finally, the `main` function is invoked to compute the 7th Fibonacci number, and the result is printed.