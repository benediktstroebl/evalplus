Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators.
    for i in range(len(operand)-1):
        for j in range(i+1, len(operand)):
            # Different operand types handling.
            if operator[i] == '*' or operator[j] == '*':
                result += operand[i] * operand[j]
            # Handling Floor Division
            if operator[i] == '/' or operator[j] == '/':
                result += operand[i] // operand[j]
            # Handling Addition and Subtraction
            if (operator[i] == '+' or operator[i] == '-') and (operator[j] == '+' or operator[j] == '-'):
                result += operand[i] % 10 * pow(10, operand[j] % 10)
                result += ((operand[j] - operand[i]) % 10) * pow(10, (operand[j] // 10 - operand[i] // 10))
            # Handling Exponentiation
            if operator[i] == '^' or operator[j] == '^':
                result += pow(operand[i], operand[j])
    return result
```
The function takes in two parameters, `operator` and `operand`, in the given problem description. It returns the result of the algebraic expression formed using the given `operator` and `operand`. The function uses nested loops to try all possible combinations of operands and operators in order to form the expression and returns the result of this expression. 

This solution focuses on simplicity and clarity. It doesn't handle some edge cases such as the possibility of having a negative number as a result or handling cases when the operand is a float number.