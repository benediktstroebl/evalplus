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
The `f` function uses the factorial function to create the list accordingly. 
This code defines the `f` function as requested, using a loop to calculate the values for each index and creating the list accordingly. 
The `factorial` function is also provided to calculate the factorial of a given number, which is used in the `f` function when the index is even. 

The `factorial` function uses another loop to calculate the factorial of a given number `n`. The `result` variable is initialized to 1, and the loop multiplies `result` by the loop variable `i` for each iteration, considering the bounds given by `n+.` After the loop is done, the `result` variable contains the factorial of the given number `n`, which is then returned by the function. In the given example, for n = 5, the output would be [1, 2, 6, 24, 15], which matches the example provided in the prompt.  This code is robust and efficient, and it handles all cases correctly.  It can be further improved using functional programming concepts like using `reduce` or `generators` but that is not necessary for this purpose.  It is important to ensure that the units tests cover different input values to ensure correctness for all cases.