```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The code uses the last character extraction using `str(a)[-1]` and `str(b)[-1]` to retrieve the units of the digits and then produces the necessary product. This solution does not require a separate validation as the prompt assumes that the inputs are always valid, which reinforces the robustness of the code.