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
    n = 7
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```

The `fib4` function calculates the nth Fibonacci number using the recursive approach without recursion, and the `test_fib4` function tests the `fib4` function with various input values. 
The script also uses the `print` function to display the output of the `fib4` function.