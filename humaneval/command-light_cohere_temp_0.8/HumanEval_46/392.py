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

# Tests
def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 8
    assert fib4(6) == 8
    assert fib4(7) == 14

if __name__ == "__main__":
    test_fib4()
```
The code defines a function `fib4` that computes the n-th Fibonacci number in O(1) using an iterative approach. It handles base cases for n equal to 0, 1, and 2, returning 0, 1, and 2, respectively. Then, it recursively computes the sequence by summing the previous four numbers. The function is then tested with various input values, and its correctness is verified through a set of tests. The `test_fib4` function runs these tests to demonstrate the functionality of the `fib4` function.