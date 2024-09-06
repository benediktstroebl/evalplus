```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a `number` as its input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (rounded down) using the `int` function. For example, `truncate_number(3.5)` returns `0.5`. 

This solution relies on understanding decimals as a fraction's numerator (the number itself) and denominator (1). In this view, subtracting the integer part corresponds to removing the largest possible integer fraction from the numerator, leaving only the smallest possible fraction (`0.5`, `0.05`, etc.) as the decimal part. 

To test this solution, you can call the function with different numbers and verify that the output is the expected decimal part. Here is an example: 
```python
truncate_number(3.5)
# Expected output: 0.5

truncate_number(2.8)
# Expected output: 0.2

truncate_number(5.01)
# Expected output: 0.01
``` 
The given solution works for any positive floating-point number. 

This approach is straightforward and works intuitively for whole numbers (e.g., 3.5 => 3 => 0.5) and behaves as required for small decimals (e.g., 0.5 => 0.05). However, it may produce slightly incorrect results for numbers closer to infinity, as Python uses `float` representations that result in progressively less accurate decimal representations. Specifically, the output would be off by a factor of 2: `0.5 => 0.25 => 0.125 => 0.0625`. 

 It's worth noting that this simplicity comes with a loss of precision and operates on the assumption that the number is a finite representation of a real number. If the input value is specially crafted to behave like infinity or doesn't exist in the traditional sense, this approach might lead to unexpected outcomes.