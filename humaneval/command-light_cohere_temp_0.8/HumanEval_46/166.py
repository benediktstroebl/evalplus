```python
def fib4(n: int):
    """The Fibonacci sequence 4 is defined as the sum of the preceding 3 terms of the sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print("Fibonacci sequence 4:")
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```
The provided Python script defines a function called fib4, which computes the n-th Fibonacci number in the 4th sequence. The function uses a series of conditional statements to determine the appropriate Fibonacci number based on the value of n. 

The if __name__ == "__main__": block allows the function to be executed when the script is run directly. The output of the script will be the three Fibonacci numbers for the inputs 5, 6, and 7, which correspond to the 4th sequence.