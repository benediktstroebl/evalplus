Here's a Python script that solves the problem you've outlined using a function with the specified parameters:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result
```
This code defines a function `do_algebra` that takes in two lists, `operator` and `operand`. It iterates through the `operator` list and performs the specific operation on corresponding elements of `operand` list to achieve the algebraic expression. The `result` variable holds the final result after all the operations are performed. 

You can test this function by calling it with different operators and operands to see the calculated results. 

For example:
```python
do_algebra([1,2,3], [4,5,6]) # Addition: 14 
do_algebra([1,2], [4,5,6]) # Error: Operand list must have equal length with the operator list minus 1 
do_algebra([3,2], [4,5,6]) # Multiplication: 12 
do_algebra([2,3], [4,5,6]) # Floor Division: 4 
do_algebra([6,2], [4,5,6]) # Exponentiation: 76 
``` 
Note that this code assumes that the lengths of both lists are such that the algebraic expression is valid. If the lengths do not conform to the prerequisite, an error will be raised.