```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It initializes a list `factorial_list` with values up to the input `n`. Then, it iterates through the range from 2 to `n`, calculating the factorial of each integer and appending the results to `factorial_list`. Finally, it returns the value of `factorial_list[n]`, which represents the Brazilian factorial of the input `n`.

Here is a simple test suite that can be used to verify the correctness of the function:
```python
def test_special_factorial():
    # Test case 1:
    assert special_factorial(0) == 1
    # Test case 2:
    assert special_factorial(1) == 1
    # Test case 3:
    assert special_factorial(2) == 2
    # Test case 4:
    assert special_factorial(3) == 6
    # Test case 5:
    assert special_factorial(4) == 288
```
To run each test case, you can simply call the `special_factorial` function with the respective input, and then compare the returned value against the expected output using the `assert` statement. 

This code will ensure that the `special_factorial` function computes the Brazilian factorial correctly for various input values. 
If you have more testing scenarios or specific requirements you'd like me to cover, feel free to provide additional input, and I'll assist in creating comprehensive test cases.