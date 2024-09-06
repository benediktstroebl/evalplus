```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly leverages the modulo operator (`%`) to determine the unit digits of both numbers, before multiplying them and ultimately resetting the product to a two-digit number if it's greater than 9. 

The function adheres to the problem's specified examples, assuming valid input as requested. It can be used as a standalone function to solve the problem. The intention is to provide a concise and direct approach to solving the problem, while still being understandable. Let me know if this aligns with your requirements or if you seek additional guidance. Feel free to supplement this code with a markdown-formatted test block for complete context.