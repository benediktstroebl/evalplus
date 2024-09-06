Here is a Python script that implements the function `f` according to the problem statement:
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

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```

This script defines a function `f` that returns a list based on the specification you provided. It also includes a nested function `factorial` to calculate the factorial of a given number `n`. The factorial function is called for the even indices and recursively calculates the factorial of each number. The `f` function builds the list accordingly for each index, whether it calculates the factorial or the sum of numbers up to that index. The provided example output shows the result for `f(5)` which matches the specified example. 

Let me know if this solves the problem for you or if you'd like further clarification on any part of the implementation. Feel free to provide another example or ask any questions regarding the problem or its solution!