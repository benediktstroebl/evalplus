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

The function `add_elements` takes an array `arr` and an integer `k` as input, and calculates the sum of elements from the first `k` entries in the array that have at most two digits. The example usage and output are also provided. Note that this code assumes decimal integers; a generalization to negative or non-decimal bases may require additional logic.

The code passes the test case presented in the question as it correctly calculates the sum of elements with at most two digits from the first 4 elements of the array ([111,21,3,4000,5,6,7,8,9] and 4). The output will be:
```
24
```