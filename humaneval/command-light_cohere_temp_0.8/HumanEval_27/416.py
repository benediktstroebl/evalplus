```python
def flip_case(string: str) -> str:
    return ''.join(''.swapcase(string))

# Test the function with various inputs and want the expected output
# test_cases = [('hello', 'hELLo'), ('world!rawr', 'WLD')
# assert flip_case(test_cases[0]) == test_cases[1]

# Main function to call the function and print the output
print(flip_case('Hello'))
```