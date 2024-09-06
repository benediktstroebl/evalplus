```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The code directly leverages the modulo operator (`%`) to determine the unit digits of both numbers, before multiplying them together. If the resulting product has a unit digit greater than 9, it resets it to 0 to ensure the final answer follows the expected format. This logic is encapsulated within a standard function, easily allowing reuse across various parts of code. 

The function adheres to the problem's specified input of two integers and returns their unit digit product, assuming valid input. 

This solution caters to the problem statement entirely within the specified single function, making it adaptable to diverse scenarios.