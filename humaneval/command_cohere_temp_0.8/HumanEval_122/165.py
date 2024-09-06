Here's a Python script that contains a function to solve the given problem:
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

This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as input. It then iterates through the first `k` elements of the array and accumulates the sum of elements that have at most 2 digits. The result is then returned as the sum of these elements. 

The example usage showcases how to use the function with the provided input. The output will be:
```bash
Example output: 24
```

This solution adheres to the given constraints.