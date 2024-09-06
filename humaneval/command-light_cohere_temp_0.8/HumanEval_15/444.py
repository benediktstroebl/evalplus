```python
def string_sequence(n: int) -> str:
    if not n:
        return 'Invalid number provided'

    if n <= 0:
        return 'Please enter a positive integer'

    result = ['0'] * n
    result[-1] = '5'

    return '\n'.join(result)

# Test the function
test_case = int(input('Enter a positive integer: '))
result = string_sequence(test_case)
print(result)
```