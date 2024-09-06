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

The function `add_elements` takes an array `arr` and an integer `k` as input, iterates through the first `k` elements of the array, and accumulates the sum of elements that have at most two digits. The resulting sum is then returned.

The example usage demonstrates how to call the function with the provided input array `arr` and value of `k` as 4, and it prints the calculated result, which matches the expected output of 24 in the problem statement.

This solution is self-contained within the provided function and will work as expected for the specified input constraints. Feel free to test it with other inputs to verify its behavior. Let me know if you have any additional questions or if you'd like to tackle more problems together!