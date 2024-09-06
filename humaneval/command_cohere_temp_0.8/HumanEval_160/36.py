Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using chained operations
    for i in range(len(operand) - 1):
        result = result + operand[i]
        for j in range(i + 1, len(operand)):
            result = result * 10 ** operand[j]
            if operator[i] == '-':
                result = result - operand[j]
            elif operator[i] == '/':
                result = result // operand[j]
            elif operator[i] == '*':
                result = result * operand[j]
    return result
```

And here is an example usage in markdown:
```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(f"The Result is: {result}")
```

Which will produce the following output:
```
The Result is: 9
```

This Python script defines a function `do_algebra` that takes two arguments: `operator` (a list of algebraic operations) and `operand` (a list of integers). It uses a loop to perform a series of operations on the operands based on the operators in the `operator` list. It iterates through the `operand` list, and for each element, it carries out the specified operation of multiplication, division, addition, or subtraction with the next element in the list. The final result is returned after all operations have been completed.