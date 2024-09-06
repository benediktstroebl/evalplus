```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the product of the unit digits is greater than or equal to 10, it returns the product modulo 10, ensuring that the result is a valid integer between 0 and 9.

This solution focuses solely on solving the specified problem statement without any additional dependencies or considerations. It's an efficient and concise implementation that directly tackles the calculation of unit digit products, making it optimized for this particular task. 

You can use this code to efficiently compute the product of the unit digits of any two integers. Feel free to customize the script to suit your specific needs and additional problem constraints. Let me know if you would like to further discuss any aspects of the solution, or if you have any other questions pertaining to solving mathematical problems, algorithms, or general programming concepts.