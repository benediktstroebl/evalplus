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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    n = 7
    assert fib4(n) == 14  # Should evaluate to true

if __name__ == "__main__":
    test_fib4()
```
This code defines a function `fib4` that computes the nth element of the Fibonacci sequence without recursion. The function uses a conditional statements to determine the base cases (0,1,2) and then uses the `fib4` function call to compute the value up to the nth element, by summing the four previous elements. 

The `test_fib4` function is used to test the `fib4` function by passing the value `n` equal to 7, which should evaluate to 14.