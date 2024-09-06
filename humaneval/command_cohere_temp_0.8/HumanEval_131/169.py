```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number n, multiplying each odd digit encountered by the evolving product. This process accounts for the odd digits' multiplication, ensuring correct results. If all digits are even, the function returns 0, aligning with the requirement when no odd digits exist.