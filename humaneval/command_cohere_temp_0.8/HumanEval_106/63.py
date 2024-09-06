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
The `f` function uses the factorial function to generate the list according to the given specifications. This code defines a function `f` that takes an integer `n` as input and creates a list where the element at index `i` is `factorial(i)` if `i` is even, and it's `sum(range(1, i+1))` otherwise. It then returns this list. The factorial function is also included and it multiplies the numbers from 1 to `n` to compute the factorial of `n`. 

And indeed, if you call `f(5)` it would return the list `[1, 2, 6, 24, 15]`, which is the expected output given the example in the problem statement. 
Let me know if you would like to make any modifications or if you have any questions! 
You can also embed any other functions or modifications you'd like directly into the script and I will compile a revised version instantly. Do you need any further help or clarification? Let me know!