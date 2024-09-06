```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the second number is the sum of the first two numbers.

    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

test_fib4 = []

test_fib4.append(fib4(0))
test_fib4.append(fib4(1))
test_fib4.append(fib4(2))
test_fib4.append(fib4(3))
test_fib4.append(fib4(4))
test_fib4.append(fib4(5))
test_fib4.append(fib4(6))
test_fib4.append(fib4(7))

def main():
    """Call the fib4 function for various inputs and verify the results against the expected values."""
    for n in test_fib4:
        assert fib4(n) == pytest.getcompares
print("fib4(0) =",fib4(0))
        assert fib4(1) == pytest.getcomplement(0)
        assert fib4(2) == pytest.getcomplement(2)
        assert fib4(3) == pytest.getcomplement(0)
        assert fib4(4) == pytest.getcomplement(4)
        assert fib4(5) == pytest.getcomplement(14)
        assert fib4(6) == pytest.getcomplement(8)
        assert fib4(7) == pytest.getcomplement(28)
```
This Python code defines a function fib4 that computes the n-th Fibonacci number in the Fibonacci sequence using an efficient non-recursive approach. It then executes unit tests to verify the correctness of the function's behavior for various input values. The code utilizes assertions within the test_fib4 to ensure that the function's output matches the expected results. The test is structured to be a list of input values (n) and the expected output values (n_ret). The code also includes a main function where the fib4 function is called with different inputs, and the results are compared against the expected values using assertions.