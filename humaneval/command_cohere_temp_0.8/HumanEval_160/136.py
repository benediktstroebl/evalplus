Here's a Python script that solves the problem you've outlined using a function called `do_algebra`:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    expect = len(operand) - 1
    for i in range(expect):
        result += operand[i]
        for j in range(oper_len):
            if operator[j] == '+':
                result += operand[i + 1]
            elif operator[j] == '-':
                result -= operand[i + 1]
            elif operator[j] == '*':
                result *= operand[i + 1]
            elif operator[j] == '//':
                result //= operand[i + 1]
            elif operator[j] == '**':
                result **= operand[i + 1]
        i += 1
    return result
```

This function takes in two parameters, `operator` and `operand`, and returns the result of evaluating the algebraic expression constructed using the given operator and operand. The function follows the requirement that the length of the `operator` list is equal to the length of the `operand` list minus one. Additionally, it assumes that the `operand` list contains non-negative integers and the `operator` list contains at least one operator and two operands. 

The function iterates through the `operand` list and performs the corresponding operation from the `operator` list at the ith index, then iterates through the `operator` list and performs the operation with the (i+1)th element in the `operand` list. Finally, it returns the computed result. 

Note that this approach assumes that the `operand` list contains static values and the `operator` list contains static operations, both of which are known ahead of time. If you're working with user-provided values and operations, you might consider adopting a different approach or incorporating additional validation and error-handling mechanisms.