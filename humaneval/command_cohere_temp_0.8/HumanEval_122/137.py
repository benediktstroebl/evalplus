Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num)) <= 2:
            sum_two_digits += num
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")
```

The function `add_elements` takes an array `arr` and an integer `k` as input, and calculates the sum of elements in the first `k` entries of `arr` that have at most two digits. The example usage and output are also provided.