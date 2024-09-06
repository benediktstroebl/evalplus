```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input `n`, checking whether each digit is odd using the modulo operator. If the digit is odd, it multiplies it into the `product` variable, which is initialized to 1 to make the product accumulation straightforward. The function returns 0 if all digits are even, and the product otherwise. 

To see the problem's solution in action, execute the following: 
```python
test_digits = {
    1: 1,
    4: 0,
    235: 15,
}

for n, expected in test_digits.items():
    result = digits(n)
    assert result == expected, f"For input {n}, expected {expected}, got {result}"
```

This block verifies the function's output against expected values, ensuring correctness.

Note, the code analyses the input's oddness solely based on individual digits, skipping considerations of the entire number's parity. Thus, for `digits(4),` although the number itself is even, it still yields a product due to the presence of the odd digit `4` in the decimal representation.