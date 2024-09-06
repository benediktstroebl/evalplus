Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using eval function
    for i in range(len(operand)-1):
        temp = operand[i]
        for j in range(i+1, len(operand)):
            temp = temp * 1
            if operator[i] == '+':
                temp += operand[j]
            elif operator[i] == '-':
                temp -= operand[j]
            elif operator[i] == '*':
                temp *= operand[j]
            elif operator[i] == '//':
                temp //= operand[j]
            elif operator[i] == '**':
                temp **= operand[j]
            result += temp
    return result
```
The following steps are used to evaluate the algebraic expression using the `eval()` function:
1. Iterate through the length of the operand list, excluding the last element (index 9).
2. Initialize a temporary variable called `temp` for each iteration, which represents a part of the expression being calculated.
3. As we iterate through the previous steps, iterate through the remaining elements of the operand list (starting from the next element) to continue building the expression.
4. Update the `temp` variable based on the arithmetic operation mentioned in the `operator` list for each set of corresponding elements in the operand and operator lists.
5. Add the updated `temp` variable to the `result` variable, which accumulates the final result.

The script assumes that the length of the `operator` list is equal to the length of the `operand` list minus one. This assumption is necessary for the function to work correctly.