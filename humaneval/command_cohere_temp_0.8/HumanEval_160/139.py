Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            temp = []
            for k in range(len(operator)):
                if operator[k] == '+':
                    temp.append(operand[i] + operand[j])
                elif operator[k] == '-':
                    temp.append(operand[i] - operand[j])
                elif operator[k] == '*':
                    temp.append(operand[i] * operand[j])
                elif operator[k] == '//':
                    temp.append(operand[i] // operand[j])
                elif operator[k] == '**':
                    temp.append(operand[i] ** operand[j])
            stack.append(temp)
    return stack[0][len(operator) - 1]
```
The function operates by iterating through the operand list and for each pair of elements, it iterates through the operator list and applies the related operations. The final element in the resultant stack is the answer. 

To verify the correctness of the function, let's add tests to the code:
```python
# Tests
def test_correct_input():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    expected = 9
    result = do_algebra(operator, operand)
    assert result == expected

def test_single_number():
    operator = ['+']
    operand = [3, 3]
    expected = 6
    result = do_algebra(operator, operand)
    assert result == expected

def test_single_operation():
    operator = ['+']
    operand = [2, 4]
    expected = 6
    result = do_algebra(operator, operand)
    assert result == expected

def test_multiple_layers():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    expected = 9
    result = do_algebra(operator, operand)
    assert result == expected

def test_negative_numbers():
    operator = ['-', '*']
    operand = [3, -4]
    expected = -4
    result = do_algebra(operator, operand)
    assert result == expected

def test_floor_division():
    operator = ['//']
    operand = [7, 2]
    expected = 3
    result = do_algebra(operator, operand)
    assert result == expected

def test_exponentiation():
    operator = ['**']
    operand = [2, 3]
    expected = 8
    result = do_algebra(operator, operand)
    assert result == expected

test_correct_input()
test_single_number()
test_single_operation()
test_multiple_layers()
test_negative_numbers()
test_floor_division()
test_exponentiation()
```
This will ensure that the function behaves as expected with a variety of input combinations. 
To execute the tests, you can use the pytest library: `pytest test_correct_input.py`  This will run all the test functions and report any failures or errors. 
The `assert` statement will automatically raise an error if the condition is not met, alerting us to a potential problem that needs to be resolved.