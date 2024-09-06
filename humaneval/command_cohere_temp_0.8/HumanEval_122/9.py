Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits

# Example usage:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

In this script, the `add_elements` function iterates through the first `k` elements of the `arr` non-empty array of integers. It accumulates the sum of elements whose string representation has at most two digits. The resulting sum is then returned.

The example usage demonstrates the function on the provided input `arr` and the specified value of `k`, printing the resulting sum of elements with at most two digits from the first `k` elements. You can append further test cases to the `arr` and `k` variables as needed to validate the function's correctness across different scenarios.