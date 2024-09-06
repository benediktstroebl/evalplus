Here is a Python script that implements the function f in a manner consistent with the problem statement:
```python
def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Test Cases
n = 5
expected = [1, 2, 6, 24, 15]
result = f(n)

print(f"For n = {n}, expected = {expected}, result = {result}")
```

This script defines a function `f` that takes an integer `n` as input and creates a list where the value at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. To calculate the factorial of a number, the script uses a recursive function `factorial` that serves as a substitute for the built-in `math.factorial` function. The script then tests the function with the provided example and prints the corresponding values. 

The output of this script is:
```
For n = 5, expected = [1, 2, 6, 24, 15], result = [1, 2, 6, 24, 15]
```
This demonstrates that the function `f` produces the expected output, as the two lists are identical.