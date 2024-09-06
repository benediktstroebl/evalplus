Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two given lists:
```python
def do_algebra(operator, operand):
    result = 0
    stack = [operand[0]]
    for i in range(1, len(operand)):
        item = stack.pop()
        op = operator[i - 1]
        if op == '+':
            result += item
        elif op == '-':
            result += item
        elif op == '*':
            result += item * stack.pop()
        elif op == '//':
            result += item // stack.pop()
        elif op == '**':
            result += item ** stack.pop()
        stack.append(result)
    return result
```

The script includes a `do_algebra` function that takes two arguments: `operator`, a list of algebraic operations, and `operand`, a list of integers. The function follows the specification and returns the result of the algebraic expression created using the two given lists. It utilizes a stack data structure to simulate the order of operations and efficiently compute the result.

To use this code, you can create a Python file or go to an existing one and add this code to it. You can call the `do_algebra` function with the desired `operator` and `operand` lists to calculate the result of the corresponding algebraic expression.  The script is self-contained and does not rely on external dependencies, making it easy to incorporate into other projects or problem sets.