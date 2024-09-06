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

The `add_elements` function takes an array `arr` and an integer `k` as input, it iterates through the first `k` elements of the array, and sums up the elements that have at most two digits when converted to a string. The result is then returned as the sum of these elements and is printed in the example usage. 

The output of the code is:
```
Example output: 24
```

This solution adheres to the specified constraints, as it handles arrays with up to 100 elements and any integer value for k (since it iterates only over the first k elements, regardless of their position in the array).