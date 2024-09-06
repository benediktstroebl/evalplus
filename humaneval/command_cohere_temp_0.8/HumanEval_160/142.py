Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The script also includes a few tests to ensure the function behaves correctly:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    assert oper_len == len(operand) - 1, "Operator list length must be equal to operand list length - 1"
    assert oper_len > 0 and oper_len == len(set(operator)), "Operator list must have unique elements"
    assert all(isinstance(i, int) and i >= 0 for i in operand), "Operand list must only contain non-negative integers"

    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]

    return result

# Tests
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
test_result = do_algebra(operator, operand)
assert test_result == 9, "Test case failed"

operator = ['*', '**', '+']
operand = [2, 3, 4]
test_result = do_algebra(operator, operand)
assert test_result == 20, "Test case failed"

operator = ['-', '+']
operand = [5, 2, 3]
test_result = do_algebra(operator, operand)
assert test_result == 0, "Test case failed"
```

To use this code, you can simply call the function `do_algebra` with your chosen `operator` and `operand` lists. The function will return the result of the algebraic expression formed from these lists, following the logic of the mathematical operations in the `operator` list.