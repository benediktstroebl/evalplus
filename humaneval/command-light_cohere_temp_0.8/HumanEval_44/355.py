```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base."""
    if base == 10:
        return str(x)
    else:
        return '{0:0b}'.format(x, base)

# Test the function
test_case1 = 8
test_case2 = 3
test_case3 = 2
test_case4 = 7
test_case5 = 10

result1 = change_base(test_case1, 10)
print(result1)

result2 = change_base(test_case2, 10)
print(result2)

result3 = change_base(test_case3, 10)
print(result3)

result4 = change_base(test_case4, 10)
print(result4)

result5 = change_base(test_case5, 10)
print(result5)

test_case6 = 'Hello, World!'
result6 = change_base(test_case6, 10)
print(result6)
```