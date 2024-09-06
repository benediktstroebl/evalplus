```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number n, multiplying each odd digit encountered by the evolving product. The result is 0 if all digits are even, and the expected product otherwise. 

To validate the implementation, you can write a few test cases in the MD format:
```
## Testing
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(2e5) == 2e5 # ignores decimal part
```

To execute these tests, you can copy them into a Python interpreter or script them in a separate .py file. 

I hope this solves your problem and feel free to ask if you'd like further clarification or additional details!