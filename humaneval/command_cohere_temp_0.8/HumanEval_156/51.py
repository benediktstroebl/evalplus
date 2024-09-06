```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Declaring the roman values map with uppercase first and then lowercase
    romans = {
        'I': 'i', 'V': 'v', 'X': 'x', 'L': 'l', 'C': 'c', 'D': 'd',
        'i': 'i', 'v': 'v', 'x': 'x', 'l': 'l', 'c': 'c', 'd': 'd'
    }
    result = []

    # Divide N into 4 tiers of 625, 125, 25, and 5
    for tier, base in enumerate([625, 125, 25, 5]):
        remain = n // base
        digit = romans[remain % 10]
        result.append(digit * (base // 25))
        n //= base

    result.reverse()
    return ''.join(result)
```

This approach divides the problem into 4 tiers based on the roman numeric system milestones of 625, 125, 25, and 5. It then iterates through the tiers, converting the remaining value into a digit and multiplying it with the base to know how many of those digits should occur in the answer (since roman numerals don't have 0s). Finally, it reverses the result to assemble the roman numeral in the correct order and joins the tiers together.