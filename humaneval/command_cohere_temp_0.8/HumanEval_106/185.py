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
```
The `f` function uses the factorial function to create the list accordingly. 
This code uses a for loop to create a list where each element is the factorial of i if i is even or the sum of numbers from 1 to i otherwise. Then, the `factorial` function calculates the factorial of a given number. 

This code should be placed in a markdown code block with the following header:
```python
```
To execute this code using a Jupyter notebook, run the cell with the code in it. However, to execute the code in a markdown file, you will need to add the execution character ("run" button) to the cell. In a Jupyter notebook, you can do this by going to "Cell" and then "Run All Cells" or "Run Selected Cells."

This should produce a list of size n with the elements computed as specified in the problem statement.