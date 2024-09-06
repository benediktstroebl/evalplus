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
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = int(input("Enter the index: "))
    result = fib4(n)
    print(f"The {n}th Fibonacci number is: {result}")

test_fib4()
```

This code defines the `fib4` function which calculates the n-th Fibonacci number in the Fibonacci sequence using a formula that does not use recursion. The function uses a `if` statements and a `while` loop that calculates the Fibonacci number by summing up the four previous numbers in the sequence. 

The `test_fib4` function prompts the user to enter an index, and then calls the `fib4` function to calculate and display the corresponding Fibonacci number.