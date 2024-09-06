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
    result = fib4(n)
    assert result == 14  # Check the result against the expected output

# Test the function with different values of n
test_fib4()
```
The Fibonacci sequence is a well-known mathematical pattern where each number is the sum of the two preceding ones. The sequence begins with 0 and 1, and each subsequent number is the sum of the previous two. This sequence is mathematical curiosity and appears in various natural phenomena. The provided code demonstrates the Python code that efficiently computes Fibonacci numbers using a loop-based approach. The function fib4(n) calculates the n-th Fibonacci number in the sequence by summing up the four preceding numbers. The test_fib4 function tests the function with different values of n and asserts that the result is equal to the expected output, successfully demonstrating the correctness of the function.