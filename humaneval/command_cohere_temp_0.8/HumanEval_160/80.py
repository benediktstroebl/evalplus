Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Compute the result using simple sequential operations
    for i in range(len(operand)):
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i]
            elif operator[j] == '-':
                result -= operand[i]
            elif operator[j] == '*':
                result *= operand[i]
            elif operator[j] == '//':
                result //= operand[i]
            elif operator[j] == '**':
                result **= operand[i]
    return result
```

This script takes two inputs: a list of operators and a list of operands. Using these two lists, the `do_algebra` function returns the result of the algebraic expression formed from these operators and the operands. All the basic algebraic operations are accounted for in the implementation. The script achieves this by employing two nested loops that iterate through both the operator and operand lists. Depending on the type of operator encountered, it adds, subtracts, multiplies, performs floor division, or raises to the power of the relevant operand to the result variable. Once the loops are complete, the result is returned. 

This code should be stored in a .py file to run properly, and that file should include a `__init__.py` file in its folder as well unless it's in a folder that's already a Python package. You can simply add your script to a .py file and run it from the command line once it has been uploaded to your Python environment.