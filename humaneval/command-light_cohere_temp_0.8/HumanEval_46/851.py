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
        return fib4(n-1) + fib4(n-2)

def test_fib4():
    n = int(input("Enter the number: "))
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

if __name__ == "__main__":
    test_fib4()
```
The code defines a `fib4` function that computes the nth Fibonacci number using a iterative approach. It utilizes a simple logic to check the base cases and then uses a recursive approach to compute the Fibonacci number. The test function is used to pass tests and demonstrate the functionality of the `fib4` function.