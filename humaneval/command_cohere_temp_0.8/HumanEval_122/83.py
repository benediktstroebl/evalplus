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
print(f"The sum of elements with at most two digits from the first {k} elements is: {result}")
```

The script provides a function `add_elements` that takes an array `arr` and an integer `k` as input, and calculates the sum of elements from the first `k` elements with at most two digits. The example usage demonstrates how to call the function with the provided input array `arr` and value of `k` as 4, and it prints the correct output, which is `24` in this case.