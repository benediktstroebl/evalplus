Here's a Python script that solves the problem you've outlined using a function called `do_algebra`:
```python
def do_algebra(operator, operand):
    result = 0
    oper_idx = 0
    for num in operand:
        if oper_idx == len(operator):
            break
        op = operator[oper_idx]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        else:
            result **= num
        oper_idx += 1
    return result
```

This script defines a function `do_algebra` that takes two arguments, `operator` and `operand`. It iterates through the integers in the `operand` list, using the next operation from the `operator` list at each iteration to process the numbers and provide the desired algebraic expression. The function returns the final result of the expression.