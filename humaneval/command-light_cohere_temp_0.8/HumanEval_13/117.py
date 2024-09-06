```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0  # To prevent division by zero
    if b == 1:
        return a
    return greatest_common_divisor(b, min(a, b))

# Test case using markdown code block
``` md
three = 5

 fifteen = 25

 sixteen = six

# Output should be 1
 greatest_common_divisor(3, 5) == 1
# 
```