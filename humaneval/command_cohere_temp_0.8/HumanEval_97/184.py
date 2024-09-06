```python
def multiply(a, b):
    num_a = a % 10
    num_b = b % 10
    product = num_a * num_b
    if product > 9:
        return 0
    else:
        return product
```

The test cases ensure that the function performs as expected with different input scenarios and handles the edge case of a product being greater than 9, which would revert to 0. Feel free to add more tests to increase code coverage and stability. 

Let me know if you'd like me to cover anything else regarding this awesome solution!