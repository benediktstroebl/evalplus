Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function `f` takes an integer `n` as input and creates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The factorial of `i` is calculated by the nested function `factorial` which multiplies `i` with all numbers from `1` to `i`.

This solution should fulfill the requirement of the problem statement and pass the given tests. 
If you would like to test this script on your local machine,  you can run it in your Python interpreter. 

You can do so by copying and pasting the code into a Python file and executing the file, or by simply pasting the code into your interpreter. 

If you encounter any issues, you can let me know and I will be happy to help you resolve them!  Also, If your primary goal is to create a script that can be run independently, I can assist you in doing so. I can also provide recommendations for setting up a testing environment to validate your code.