```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is similar to the Fibonacci sequence but starts from a different origin, so it's also known as the Fib4 sequence.
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Fibonacci sequence using the fib4 function"""
    print("Fibonacci sequence: ", end="")
    for i in range(5):
        print(fib4(i), end=" ")
    print()

test_fib4()
```
The code defines a function `fib4` which computes the nth element of the Fibonacci sequence using the formula `F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`. The `test_fib4` function then calls `fib4` to print the first five elements of the Fibonacci sequence.