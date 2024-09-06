```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as inputs and returns the product of their unit digits. The unit digit is the digit at the farthest right of the number. For example, the unit digit of 123 is 3. This is achieved by using the built-in function `str` to convert both input integers to strings, accessing the last character (the unit digit) using `[-1]`, then converting it back to an integer using int() and multiplying the results. 

Let's take the examples provided in the prompt to test the function:
- `multiply(148, 412)` returns `16` because the unit digits are `8` and `2`, respectively, and their product is 16. 
- `multiply(19, 28)` returns `72` because the unit digits are `9` and `8`, respectively, and their product is 72. 
- `multiply(2020, 1851)` returns `0` because both numbers have 0 as their unit digit. 
- `multiply(14, -15)` returns `20` because the unit digits are `4` and `5`, respectively, and their product is 20. 

The function successfully computes the product of the unit digits of the given integers, assuming the input is always valid, as stipulated in the prompt.