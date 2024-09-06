Here is a Python script that solves the problem you have described:
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
```
The above code contains two functions: the `f` function accepts `n` as a parameter and returns a list according to the problem statement, and the `factorial` function calculates the factorial of a given number `n`. 

The `f` function iterates through numbers from 1 to `n` and according to the parity of each number, it either appends its factorial or the sum of numbers from 1 to `i` to the list `li`. 

I have also included a `factorial` function since it is used in the description of the problem you have provided, however, you are not required to include it in your portfolio since it is not explicitly asked for. 

The code passes the given example test case for `f(5)`, as it returns the list [1, 2, 6, 24, 15]. 
Let me know if you would like me to transform this code into a standalone module or if you'd like me to structure it as an ESLint-compliant code block. 

I can also suggest other improvements to help you structure this code neatly and adhere to best practices. eva