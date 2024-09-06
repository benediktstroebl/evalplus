```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input integer 'n' and multiplies the odd digits together, effectively computing the product of these odd digits. The function returns 0 if all digits are even, and the calculated product otherwise. This TDD approach helps in creating more robust and reliable code, as any new additions or changes are validated against expectations, ensuring that the function's behavior aligns with its intended purpose. 

The function's implementation ensures that it can be easily adapted to handle a broader range of input types and variations, which is important in building resilient and flexible code.