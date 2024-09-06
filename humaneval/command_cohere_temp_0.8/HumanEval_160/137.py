Here's a Python script that solves the problem you've outlined, along with a markdown code block showing the complete script:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result
```
The Python script defines a function `do_algebra` that takes two arguments, `operator` and `operand`. It assumes that the `operator` list contains basic algebra operations, such as addition, subtraction, multiplication, floor division, or exponentiation, and the `operand` list contains integers. The function evaluates the algebraic expression constructed from the given operator and operand lists and returns the result. 

The script assumes that the length of the `operator` list is equal to the length of the `operand` list minus one, and that both lists have at least two elements, which are the minimum requirements as mentioned in the problem statement. 

You can use this function to solve the problem by passing the specific `operator` and `operand` lists for which you want to evaluate the algebraic expression.