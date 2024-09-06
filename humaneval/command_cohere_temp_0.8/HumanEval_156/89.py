```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, tens, units = divmod(n, 1000)
        return int_to_mini_roman(hundreds) + int_to_mini_roman(tens) + str(units)
```

The hundreds place is computed by dividing `n` by 1000 and taking the remainder. This division and modulo operation (often abbreviated as "divmod" in Python) extracts the three relevant numbers for rendering: hundreds, tens, and units.

The tens and units are processed directly as integers, but the hundreds are handled recursively, leading to a concatenated string representation of the number in Roman numerals. 

This approach adheres to the problem's specifications of converting numbers between 1 and 1,000 to mini Roman numerals in lowercase. 

If you'd like, we can dive deeper into any of the concepts involved or explore other relevant examples! Let me know!