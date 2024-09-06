```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    return: n
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(fib4(n))
```

This code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a specific formula. It uses an if-elif structure to determine the base cases for the sequence (0, 1, and 2) and recursively computes subsequent numbers. The function returns the value of n. The main function then takes user input, calls the fib4 function with the input, and prints the result.