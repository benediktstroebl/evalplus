Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators.
    for i in range(len(operand)-1):
        for j in range(i+1, len(operand)):
            # Handling exponentiation with both variables as the base.
            if operator[i] == '**' and operator[j] == '**':
                result += operand[i] ** operand[j]
            # Handling exponentiation with only first variable as the base.
            elif operator[i] == '**':
                result += operand[i] ** operand[j] * operand[i]
            # Handling exponentiation with only second variable as the base.
            elif operator[j] == '**':
                result += operand[i] * operand[j] ** operand[i]
            # Handling all other cases.
            else:
                result += eval(f'{operand[i]}{operator[i]}{operand[j]}')
    return result
```
The script uses nested loops to iterate through all possible pairs of operands and operators, it then uses Python's eval function to construct and evaluate the corresponding algebraic expressions. Finally, the function returns the result of the computed expression. 

To use this code, you can simply call the `do_algebra` function with the `operator` and `operand` lists as arguments, the output will be the solution to the provided problem.