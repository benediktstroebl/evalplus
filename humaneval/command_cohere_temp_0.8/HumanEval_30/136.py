Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a list of all positive numbers in the input list `l`.

To test this function, you can use the following code:
```python
test1 = [-1, 2, -4, 5, 6]
test2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(test1))  # Expected output: [2, 5, 6]
print(get_positive(test2))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This will print the expected output for each test case, verifying that the function behaves as expected.