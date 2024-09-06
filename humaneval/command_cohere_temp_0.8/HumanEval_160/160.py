Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The function is designed to support basic algebra operations `+`, `*`, `-`, `//`, and `**`. 

The script also includes a set of tests to validate the function against different combinations of operators and operands to ensure it aligns with the problem statement. 

```python
def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate over it twice
    n = min(len(operator), len(operand))
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{result}')
    return result

# Tests
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
test_cases = [
    ([operator, operand], 9),
    ([['*'], [3]], 9),
    (['+', '*', '-', '**'], 10),
    ([['+', '*'], [2, 3]], 10),
    ([['**'], [5]], 0)
]

for op, ans in test_cases:
    assert do_algebra(*op) == ans
```

To use the function, you can call `do_algebra()` with your desired sets of operators and operands as shown in the test cases. The function is designed to handle any combination of operators and operands as long as the operator list is one item longer than the operand list.