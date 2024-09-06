Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            item = operand[i]
            for k in range(j + 1, len(operand)):
                item = operator[k - j - 1](item, operand[k])
            stack.append(item)
    return stack[0]
```

The script includes a function called `do_algebra` that takes two lists, `operator` and `operand`, as input. It uses the operands and applies the operations in the `operator` list to return the result.

Let's break down the steps of the algorithm:
1. Create a variable `stack`, which is an empty list where the resultant value will be stored.
2. Iterate through the length of the `operand` list, less one, as the last element in the list is considered as the result of the algebraic expression. Consider the  `i`th  element in the `operand` list, and iterates from `i+1` to the end of the list.
3. For each element in the above loop, take the  `i`th  element of the `operand` and loop from `j+1` to the end of the list to check the remaining elements in the list and make the operation.
4. Inside the nested loop, an element is calculated by using the `operand` list value and the `operator` list to update the `item` variable.
5. After the operation is done, the updated `item` value is appended to the `stack` list.
6. Finally, return the first element of the `stack` list as the result of the algebraic expression. 

This algorithm uses a nested loop to iterate through all possible combinations of operands and operators, building up a stack of operations to calculate the result. 

Note: Due to the use of recursion in this approach, it is not the most efficient approach considering the excessive number of function calls. Instead, a solution using a loop with less function calls would be more efficient for this problem. 

This script can be used as a self-contained function to solve the problem described in the prompt.