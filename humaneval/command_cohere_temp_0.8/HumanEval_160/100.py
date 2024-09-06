Here's a Python script that solves the problem you've outlined, along with a few example tests to ensure the function works as expected:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operator[i] * operand[i]
    return result

# Tests
assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
assert do_algebra(['*', '/'], [4, 2]) == 2
assert do_algebra(['+', '-', '*'], [5, 3, 2]) == 14
assert do_algebra(['**', '*'], [2, 3]) == 8
```

In the self-contained `do_algebra` function, we iterate through the length of the `operator` list, and perform the corresponding operation of the operator on the `operand` list. The result is accumulated accordingly. The provided tests cover different scenarios of the algebra operations, their combinations, and verify that the function's output matches the expected results. avier with your code and let me know if you'd like me to cover any other topics related to Python, software development, or mathematics!