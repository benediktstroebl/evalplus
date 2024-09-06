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

This script defines a function `add_elements` that takes an array `arr` and an integer `k` as input, it initializes a variable `sum_two_digits` to 0 and iterates through the first `k` elements of the array. If the length of the string representation of an element is less than or equal to 2, its value is added to the `sum_two_digits`. Finally, the function returns the calculated sum.

The example usage provided demonstrates how to call the function with the given array and value of `k`, and the output is printed accordingly.