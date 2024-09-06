Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The `add_elements` function iterates through the first `k` elements of the `arr` non-empty array of integers. It adds the elements whose string representation has at most two digits to the `sum_two_digits` variable. The function returns the computed sum. 

The example usage is provided in the script and should print out the following output:
```bash
Example output: 24
```

This approach solves the challenge by considering the length of the string representation of each number, instead of explicitly converting the integers to strings and counting the digits.