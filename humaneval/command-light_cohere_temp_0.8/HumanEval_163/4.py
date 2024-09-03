```python
def generate_even_digits(limit):
    digits = []
    while True:
        n = 2 * limit
        if n <= limit:
            digits.append(str[n])
    return digits

# Test cases
test_case1 = generate_even_digits(8)
test_case2 = generate_even_digits(10)
test_case3 = generate_even_digits(14)

print("Test case 1:", test_case1)
print("Test case 2:", test_case2)
print("Test case 3:", test_case3)
```
This code defines the function `generate_even_digits`, which generates a list of even digits up to a given integer `limit`. It uses a loop that creates even numbers until the number is less than or equal to `limit`, at which point it appends the even digit to the list. 

The test cases are then generated using the function with different `limit` values, and the results are printed.