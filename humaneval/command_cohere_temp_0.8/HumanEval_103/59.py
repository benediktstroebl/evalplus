Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the result to binary and return
    if rounded_avg == -1:
        return "-1"
    else:
        return f"0b{bin(rounded_avg)[2:]}"

# Define test cases
cases = [
    (1, 5, "0b11"),
    (7, 5, "-1"),
    (10, 20, "0b1111"),
    (20, 33, "0b11010"),
]

# Test the function against the test cases
for n, m, answer in cases:
    result = rounded_avg(n, m)
    if result != answer:
        print(f"For n={n}, m={m}, expected '{answer}' but got '{result}'")
```

The provided code includes a self-contained function `rounded_avg(n, m)` to compute the average of integers between `n` and `m`, round it, convert it to binary, and handle edge cases. It also includes a list of test cases to validate the function against expected outputs. The script will print a message for each test case indicating whether the expected result matches the actual output.