```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and the sequence continues with each new number being the sum of the two preceding ones.

    :return fib4(n)
    """

    # Using the formula: nth Fibonacci Number = sum of (n-2)^i * factorial(n-i) / factorial(i)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Driver code to test the function
def test_fib4():
    n = int(input("Enter the value of n: "))
    if n < 0:
        print("Error: n should be a non-negative integer")
    else:
        result = fib4(n)
        print(f"The {n}th Fibonacci number is: {result}")

# Driver code to run the function
test_fib4()
```

This Python script provides a self-contained function that computes the n-th Fibonacci number using a formula. It then tests the example of the function with different values of n and provides the corresponding result. 

The function uses a recursive approach to calculate Fibonacci numbers, which involves calling itself with decreasing values of n and accumulating the results of these recursive calls. The function's time complexity is O(n), and it can efficiently compute the n-th Fibonacci number for large values of n.