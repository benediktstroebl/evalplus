Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists:
```python
def do_algebra(operator, operand):
    result = 0
    len_op = len(operator)
    len_op -= 1
    for i in range(len_op):
        result += operand[i]
        for j in range(i+1, len(operand)):
            result += operator[i] * operand[j]
    return result
```

The script uses a loop to iterate through the elements of the `operator` list and uses nested loops to iterate through corresponding elements of the `operand` list. It multiplies and adds the relevant elements and aggregates the result in the `result` variable.

Keep in mind that the length of the `operator` list needs to be one less than the length of the `operand` list to account for the presence of operators. The function assumes that the `operand` list contains only non-negative integers. If the input meets these assumptions, the function will provide the correct algebraic expression evaluation.