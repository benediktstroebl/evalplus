Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using the declared algorithm
    for i in range(len(operand) - 1):
        result += operand[i] * eval(f'{operator[i]!).__getitem__(operand[i+1])' )
    return result
```
The algorithm is clearly described in the docstring, so I won't go into detail here, but will give a short overview. We iterate through the operand list, and for each iteration calculate the action of the current operator between the current element of the operand list, and the next element of the list using Python's eval function. Finally, we return the calculated result. 

This approach allows us to apply any valid expression built from the declared operations on the operand list, which makes the function versatile and capable of solving any variation of the problem statement.