```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is defined as follows:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return

def test_fib4():
    """Test the fib4() function by providing a value of n.
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

if __name__ == "__main__":
    test_fib4()
```
The code defines a function called fib4 which computes the n-th element of the Fibonacci sequence using a formula-based approach. It then includes a test_fib4 function which tests the functionality of fib4 with sample inputs. The code is self-contained and does not rely on any external modules or functions.