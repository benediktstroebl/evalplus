```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers in the range from 1 to `n` (inclusive). The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum of the integers from 1 to `n` as the result. 

This function is used to solve the problem of summing integers from 1 to a given number 'n' and is encapsulated within a function, making it reusable and modular, allowing it to be easily integrated into larger programs when needed. 

You can use the function by calling it with different values for 'n' and comparing the returned values with the expected sums to ensure the function behaves as expected:
```python
# Test the function with different inputs
n = 5
expected_sum = 15
result = sum_to_n(n)
print(f"Test n = {n}: Expected sum = {expected_sum}, Actual sum = {result}")

n = 10
expected_sum = 55
result = sum_to_n(n)
print(f"Test n = {n}: Expected sum = {expected_sum}, Actual sum = {result}")

n = 30
expected_sum = 465
result = sum_to_n(n)
print(f"Test n = {n}: Expected sum = {expected_sum}, Actual sum = {result}")

n = 1
expected_sum = 1
result = sum_to_n(n)
print(f"Test n = {n}: Expected sum = {expected_sum}, Actual sum = {result}")

n = 100
expected_sum = 5050
result = sum_to_n(n)
print(f"Test n = {n}: Expected sum = {expected_sum}, Actual sum = {result}")
```

This demonstrates the operation of the `sum_to_n` function with different test cases, ensuring that it accurately computes the sum of integers from 1 to 'n' as expected.