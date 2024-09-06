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
    """Test the fib4 function.
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Error: Input must be a positive integer.")
    else:
        result = fib4(n)
        print(f"The {n}-th Fibonacci number is {result}")

test_fib4()
```
This Python script defines a function called fib4 which computes the n-th Fibonacci number in a sequence using an iterative approach. 

The function uses a base case and a series of conditional statements to calculate the result. 

The test_fib4 function is designed to verify the correctness of the fib4 function by taking user input and displaying the result.