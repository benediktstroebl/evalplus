Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The script also includes a set of tests to ensure the function behaves as expected:
```python
def do_algebra(operator, operand):
    result = 0
    opera_len = len(operator)
    it = iter(operand)
    for i in range(opera_len):
        result += next(it) * eval(f'{operator[i]}{result}')
    return result

# Tests
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
test_case = 2 + 3 * 4 - 5
assert do_algebra(operator, operand) == test_case

operator = ['*', '++']
operand = [3, 7, 2]
test_case = 3 * (7 + 2)
assert do_algebra(operator, operand) == test_case

operator = ['-', '+']
operand = [10, 5, 2]
test_case = 10 - 5 + 2
assert do_algebra(operator, operand) == test_case

operator = ['**', '+', '*']
operand = [2, 3, 4, 5]
test_case = (2 + 3) * 4 ** 5
assert do_algebra(operator, operand) == test_case
```

You can add more tests to this block to cover more scenarios.