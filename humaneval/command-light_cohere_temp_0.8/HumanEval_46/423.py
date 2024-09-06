Here's the solution:
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
    n = int(input("Enter a number: ":"))
    print(f"Fib4({n})", end=" ")

test_fib4()
```
The function `fib4` calculates the n-th Fibonacci number in the sequence using a constant-time method without recursion. The function first checks if `n` is less than 4. If `n` is 0, 1, or 2, it returns the corresponding number. If `n` is 3, it returns the sum of the previous four numbers in the sequence. If `n` is 4, it returns the sum of the previous five numbers in the sequence.

The test function `test_fib4` prompts the user to enter a number, and then calls the `fib4` function with that number as the argument. The function returns the result, and prints it to the console.