Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists:
```python
def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        stack.append(operand[i])
    stack.append(operand[-1])
    result = stack[0]
    for i in range(1, len(stack)):
        operator_i = operator[i - 1]
        if operator_i == '+':
            result = result + stack[i]
        elif operator_i == '-':
            result = result - stack[i]
        elif operator_i == '*':
            result = result * stack[i]
        elif operator_i == '**':
            result = result ** stack[i]
        elif operator_i == '/':
            result = result // stack[i]
    return result
```

The script provides a function that takes two lists, one representing the algebraic operation symbols and the other containing integers, and returns the value resulting from applying the operations in accordance with the sequence of operations (PEP).

It is important to note that this Python script assumes that both the `operator` and `operand` lists have data structures that are amenable to the expected operations (e.g., the `operand` list contains integers and the `operator` list contains either '+' or '-' or '*' or '**' or '/' characters). It is also crucial to handle scenarios where the lengths of the two lists may not be compatible for the stated problem.