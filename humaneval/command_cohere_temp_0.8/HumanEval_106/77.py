Here is a Python script that solves the problem you have described:
```python
def f(n):
    li = [0] * n
    for i in range(1, n+1):
        if i % 2 == 0:
            li[i-1] = factorial(i)
        else:
            li[i-1] = sum(range(1, i+1))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The `f` function generates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. To do this, it iterates through each index in the range from 1 to `n` (`n` is the length of the list), and fills in the corresponding value. The `factorial` function calculates the factorial of a given number `n` by iterating through all numbers from 1 to `n` and multiplying them together. It starts with a result value of 1 and keeps multiplying by the current number (`i`) in the loop, updating the 'result'. 

This code should be stored in a markdown code block, and it will solve the problem you have described. Let me know if you would like any adjustments to the code or explanations!