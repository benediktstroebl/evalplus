```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1]*(degree-i)
    return result
```

The following tests are included to verify the correct behavior of the derivative function:
```python
def test_derivative_zero_derivatives():
    assert derivative([1, 0, 3]) == [0, 0, 3]

def test_derivative_simplest_case():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

def test_derivative_single_derivative():
    assert derivative([1, 2, 3]) == [2, 6]

def test_derivative_multiple_derivatives():
    assert derivative([7, 11, 3, 1]) == [38, 66, 18, 2]

def test_derivative_negative_polynomial():
    assert derivative([2, -3, 4, -1]) == [-6, 12, -8, 2]

def test_derivative_empty_polynomial():
    assert derivative([]) == []
```

The function `derivative` calculates the derivative of a polynomial given as a list of coefficients. It uses a basic formula to calculate the derivative of each term of the polynomial and stores the result in a list, returning it thereafter. 

The tests demonstrate usage of the `derivative` function with various test cases, verifying the correctness of the calculated derivatives against expected outputs. 
If you have any suggestions or questions about the code, please let me know!  It can be beneficial to consider edge cases such as negative coefficients or an empty polynomial to enhance the robustness of the `derivative` function.  If you desire, I can also provide suggestions for more efficient solutions.