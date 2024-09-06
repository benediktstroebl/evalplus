Here's a Python script that solves the problem you've outlined using a function called `do_algebra`:
```python
def do_algebra(operator, operand):
    result = 0
    oper_idx = 0
    for num in operand:
        result += operator[oper_idx] * num
        oper_idx += 1
    return result
```

This script defines a Python function called `do_algebra` that takes in two lists, `operator` and `operand`. It assumes that these lists have the same length for the sake of simplicity, and it returns the result of evaluating the algebraic expression constructed from the provided operator and operand lists. 

The script assumes that the `operator` list contains basic algebra operations as specified in the problem, and the `operand` list contains integers. It is further assumed that these integers are non-negative. The script then iterates through the `operand` list, and accumulates the result of each element in the list with the respective operator, following the order of operators provided in the `operator` list. 

This simple approach solves the problem, and the output of the function is the result of the algebraic expression constructed with the provided operators and operands. 

Please note that this script is providing a straightforward solution for the specified problem. If you have additional constraints or complexities, it may require a adapted approach.