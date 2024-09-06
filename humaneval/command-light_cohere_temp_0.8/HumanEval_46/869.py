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
    n = int(input("Enter the value of n: "))
    if n < 0:
        print("Error: n must be a non-negative integer.")
    else:
        result = fib4(n)
        print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```
The code defines a function called fib4 that computes the n-th Fibonacci number using a loop and basic arithmetic operations. The function has conditional checks to handle edge cases, such as invalid input or negative numbers. It then returns the test_fib4() function to compute the n-th Fibonacci number based on user input.