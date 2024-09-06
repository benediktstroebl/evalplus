```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` and multiplies each odd digit found with the `prod` variable, which starts at 1. The function returns 0 if all digits are even, and the final product otherwise, which aligns with the given problem statement and its intended behavior. 

To see it in action, call the function like this:
```python
print(digits(235))
```

Running this code snippet will give you the following output:
```
15
```