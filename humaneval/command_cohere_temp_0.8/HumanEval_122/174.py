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

The function `add_elements` takes an array `arr` and an integer `k` as input, and iterates through the first `k` elements of the array. It extracts the integer at each step and checks the length of its string representation. If this length is <= 2, the integer is added to the running total `sum_two_digits`. The function returns the total of all such integers.

The example usage demonstrates how to call this function with a sample array and value for k, printing the result to the console.