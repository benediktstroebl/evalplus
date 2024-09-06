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

The code defines a function `add_elements` that takes in an array `arr` and an integer `k` as input and calculates the sum of elements in the first `k` entries of the array that have at most two digits.

The example usage demonstrates how to call the function with the provided input array `arr` and value of `k` as 4, and it prints the calculated result. The output of the script is:
```
Example output: 24
```

This sum is achieved by the loop in the function, which iterates over the first `k` elements of `arr` and accumulates the sum of elements that have a length of at most 2 when converted to a string, as specified by the problem statement.