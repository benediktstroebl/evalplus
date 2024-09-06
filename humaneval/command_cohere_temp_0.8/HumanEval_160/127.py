Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly
    exp_op = operator.pop() if operator and operator[-1] == "**" else None
    for op in operator:
        if op == "+" : result += operand.pop()
        elif op == "-" : result -= operand.pop()
        elif op == "*" : result *= operand.pop()
        elif op == "/" : result //= operand.pop()
        elif exp_op: result = result ** operand.pop()
        else: return "Error! Invalid operator %s in the list of operators!" % op
    return result
```

The function operates by repeatedly executing the topmost operation in the list of operators, using the two most recent elements in the list of operands. When an exponentiation operator is encountered, it is handled explicitly, bailing from the loop and iterating operand list. The function finishes by returning the final value of the resulting expression. 

Note, the algorithm assumes that the list of operands is sorted, which is not mentioned in the Problem Description. Thus, the algorithm may produce a wrong result if the list of operands is not sorted.