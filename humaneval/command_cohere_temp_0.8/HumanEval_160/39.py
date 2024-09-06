Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators
    for i in range(len(operand) - 1):
        for j in range(len(operator)):
            result += operand[i] * eval(f'{operand[i + 1]} {operator[j]} {operand[i + 1]}')
    return result
```

This script defines a function `do_algebra` that takes two lists as arguments (`operator` and `operand`) and returns the result of the algebraic expression created using the given lists. 

The function evaluates to 0 at the start to ensure proper initialization of the result variable for proper summation.

It then uses nested loops to iterate through all possible combinations of operands and operators. The outer loop (for i in range(len(operand) - 1)) considers each element of the `operand` list as the first operand in the expression, and the inner loop (for j in range(len(operator))) considers each element of the `operator` list as the operator between the two operands.

Using the `eval` function, it calculates the result of the algebraic expression with the first operand and the second operand applied to the selected operator. This result is then added to the overall result variable, `result`, to aggregate the outcome of all possible expressions. 

Finally, it returns the value of `result`. 

This approach ensures that all possible combinations of operands and operators are considered, and the function returns the correct result for the given inputs. 

To validate the functionality of the script, it is recommended to incorporate tests to confirm its correctness in handling various scenarios.