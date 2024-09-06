Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The function `add_elements` takes an array `arr` and an integer `k` as input, it iterates through the first `k` elements of the array and calculates the sum of elements that have at most two digits. The example usage and output are also provided. Feel free to uncomment the test case to verify the function against your specific constraints.