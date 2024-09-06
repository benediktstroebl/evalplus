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

The function `add_elements` takes an array `arr` and an integer `k` as input and iterates through the first `k` elements of the array. It extracts the integer at each step and checks the length of its string representation. If this length is less than or equal to 2, the integer is added to the sum `sum_two_digits`. The function returns the final sum of all the integers with at most two digits.

The example usage demonstrates how to call the function with the provided input array `arr` and value of `k` as 4. The result is then printed out.