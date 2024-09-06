```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem. It initializes a list `factorial_list` with values of factorials from 1! to n!. Then, it computes the `factorial_list` iteratively, where each element at index `i` is calculated as `i * factorial_list[i - 1]`. Finally, it returns the value of `factorial_list[n]`, which is the Brazilian factorial of `n`.

Here is a simple test suite that verifies the correctness of the `special_factorial` function:
```python
def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 2450
```
This test suite uses the `assert` statement to verify that the output of `special_factorial` is correct for different input values (`0`, `1`, `2`, `3`, `4`, and `5`).  This assertion checks the correctness of the `special_factorial` function, ensuring that it aligns with the definition of the Brazilian factorial. 

To run the test suite, you can call the `test_special_factorial()` function within the Python interpreter:
```python
test_special_factorial()
```

Or, alternatively, you can run the script file containing the test suite if it's separately executable:
```bash
python test_special_factorial.py
```

Conducting these tests ensures that the `special_factorial` function produces the expected outputs for the given input values, validating the proper operation of the function.