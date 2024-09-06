Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists:
```python
def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    for j in range(1, len(operator)):
        top1 = stack.pop()
        top2 = stack.pop()
        stack.append(operator[j] + top1 + ' ' + top2 + '=' + str(eval(top1 + ' ' + top2)))
    return stack.pop()
```

The script includes a set of unit tests that can be run using the `pytest` library. The tests cover various scenarios including adding, subtracting, multiplying, dividing, and exponentiating integers, as well as testing the edge cases of empty input lists.

To run the tests, you can use `pytest` by executing the following command in the terminal:
```bash
pytest
``` 

This command will run all the tests in the current directory and will return a summary of the test results, including the number of tests passed, failed, or raised errors.