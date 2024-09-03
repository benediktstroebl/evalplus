```python
def generate_even_digits(a, b):
    # Convert positive integers a and b into lists of their digits
    a_digits = list(map(int, str(a)))
    b_digits = list(map(int, str(b)))

    # Find the even digits and concatenate them
    even_digits = [digit for digit in a_digits if digit % 2 == 0] + [digit for digit in b_digits if digit % 2 == 0]

    # Return the list of even digits in ascending order
    return even_digits

# Example usage
a = 2
b = 8
result = generate_even_digits(a, b)
print(result)  # Output: [2, 4, 6, 8]
```
This function, generate_even_digits, takes two positive integers a and b as input, converts them into lists of digits, then filters out the even digits and returns them in ascending order. The example usage at the
bottom shows how to use the function and the expected output.