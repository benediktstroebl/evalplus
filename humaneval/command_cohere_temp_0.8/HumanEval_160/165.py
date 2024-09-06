Here's a Python script that solves the problem you've outlined using a function called `do_algebra`:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i]
        for j in range(i+1, len(operand)):
            result += operand[j] * operator[i]
            if operator[i] == '/':
                result //= operand[j]
            if operator[i] == '^':
                result **= operand[j]
        if operator[i] == '-':
            result -= operand[j]
    return result
```

This script defines a Python function called `do_algebra` that takes in two parameters, `operator` and `operand`. It returns the result of the algebraic expression constructed from the given operator and operand. The script assumes that the lengths of both `operator` and `operand` are such that the result of the expression is deterministic.