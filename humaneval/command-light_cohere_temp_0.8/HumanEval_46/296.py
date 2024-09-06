```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which the first two are 0 and 1, and each subsequent number is the sum of the previous two.

    The sequence follows the Fibonacci numbers, a series in which each number is the sum of the two preceding ones.

    Parameters: n:
        An integer representing the index of the Fibonacci number to be calculated.
    Returns: The Fibonacci number at the given index.

# Test cases
if __name__ == "__main__":
    n = int(input("Enter the index: "))
    if n <= 0:
        print("Index must be a positive integer.")
    else:
        result = fib4(n)
        print(f"Fibonacci({n}) = {result}")
```