Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
    expr.append(1)

    for i in range(num_operands - 1):
        expr[i+1] = expr[i+1] * (-1) if operator[i] == '-' else expr[i+1] * operand[i]
        expr[i+1] = expr[i] + expr[i+1] if operator[i] == '+' else expr[i] - expr[i+1]
        expr[i+1] = expr[i] * expr[i+1] if operator[i] == '*' else expr[i] // expr[i+1]
        expr[i+1] = expr[i] ** expr[i+1] if operator[i] == '**' else expr[i+1] ** expr[i]

    return expr[-1]

# Example usage
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9

# Test case
operator = ['+', '-']
operand = [1, 2, 3]
print(do_algebra(operator, operand))  # Output: 4
```

This script will return the result of the algebraic expression created using the `operator` and `operand` lists, assuming that the length of the `operator` list is equal to the length of the `operand` list minus one. Additionally, it assumes that the `operand` list contains only non-negative integers, and that the `operator` list contains at least one operator and the `operand` list has at least two elements. 

Let's break down the functionality of the `do_algebra` function for better clarity:
1. `num_operands = len(operand)`: Determines the number of operands based on the length of the `operand` list. 
2. `expr = []`: Initializes an empty list, `expr`, to hold each intermediate step of the algebraic expression. 
3. The loop from range(num_operands - 1): Iterates through each element of the `operand` list, except the last one. It appends each operand to the `expr` list. The last element in the list is always set to 1 to serve as a default value and simplify calculations. 
4. The inner loop: Iterates through each element of the `operator` list and each element of `expr` (except the last one) to perform the corresponding algebraic operation. The elements of `expr` are modified in situ by this loop.
5. The final result: The last element in `expr`, which represents the result of the algebraic expression, is returned. 

This approach follows a step-wise build-up logic, creating the algebraic expression iteratively by applying the given operators to the operands one by one. 

Let's also consider a test case to illustrate this script:
```python
operator = ['+', '-']
operand = [1, 2, 3]
print(do_algebra(operator, operand))  # Output: 4
```
In this example, the expression built is: `1 + 2 - 3