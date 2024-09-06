Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    result = stack.pop()
    for i in range(len(operator)):
        operator = operator[i]
        if operator == '+':
            result += stack.pop()
        elif operator == '-':
            result -= stack.pop()
        elif operator == '*':
            result *= stack.pop()
        elif operator == '**':
            result **= stack.pop()
        elif operator == '/':
            numerator = stack.pop()
            denominator = stack.pop()
            result = numerator // denominator
        else:
            return "Error: Invalid operator"
    return result
```

The algorithm for the function works as follows:
1. Create a stack and iterate through the `operand` list, pushing each element onto the stack.
2. Remove the last item from the stack and store it in the `result` variable.
3. Iterate through the `operator` list, performing the corresponding operation on the two top elements of the stack:
    - For addition (`+`) and subtraction (`-`), pop two elements from the stack and apply the operation.
    - For multiplication (`*`), pop two elements and multiply them.
    - For exponentiation (`**`), pop an element, raise it to the power of the second element, and multiply them.
    - For division (`/`), pop the numerator and denominator, and divide them.
4. After processing all operations, return the final value of `result`.

This approach follows a typical approach for evaluating algebraic expressions using operator precedence and follows the logic required in the problem description.