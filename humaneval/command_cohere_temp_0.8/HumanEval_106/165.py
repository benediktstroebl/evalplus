Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    li = []
    for i in range(1, n+1):
        if i % 2 == 0:
            li.append(factorial(i))
        else:
            li.append(sum(range(1, i+1)))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```
The `f` function uses a list comprehension to create a list where the value at index `i` is the `factorial` of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function is defined to calculate the factorial of a given number using a loop. The provided test case prints the output for `f(5)` as requested in the prompt, confirming that the function correctly solves the problem.