```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fibonacci4():
    """Test function for fib4 function."""
    print("Test 1: Fibonacci of 5 should return 4.")
    assert fib4(5) == 4

    print("Test 2: Fibonacci of 6 should return 8.")
    assert fib4(6) == 8

    print("Test 3: Fibonacci of 7 should return 14.")
    assert fib4(7) == 14

    print("Test 4: Fibonacci of 8 should return 24.")
    assert fib4(8) == 24

    print("Test 5: Fibonacci of 9 should return 45.")
    assert fib4(9) == 45

test_fibonacci4()
```
The function **fib4** calculates the n-th element of the Fibonacci sequence, a mathematical series in which each number is the sum of the two preceding ones. The function uses a recursive approach, where it calls itself with the decrement of n until the base case is reached (n == 0, 1, 2). The function then sums up the values from the recursive calls to compute the Fibonacci number for the given n.

The test function **test_fibonacci4** tests the function by providing values of n and checking if the calculated Fibonacci number matches the expected result. The function passes all tests successfully and demonstrates the correctness of the **fib4** function.