```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
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
    """Test the fib4 function"""
    print(fib4(5))  # Output should be 4
    print(fib4(6))  # Output should be 8
    print(fib4(7))  # Output should be 14

if __name__ == "__main__":
    test_fib4()
```
The code defines the **Fibonacci sequence** with a simple mathematical formula and then tests the function using the `test_fib4` function. It should pass the Recursion and mathematical accuracy should be taken into account.