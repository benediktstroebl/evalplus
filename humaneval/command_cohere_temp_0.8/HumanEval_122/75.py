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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

The function `add_elements` takes an array `arr` and an integer `k` as input, iterates through the first `k` elements of the array, and accumulates the sum of elements that have at most two digits. The resulting sum is then returned.

The example usage demonstrates how to call the function with the provided input array `arr` and value of `k` as 4. The output will be:
```bash
The sum of the elements with at most two digits from the first 4 elements is: 24
```

This solution is efficient with a time complexity of O(K), where K is the input integer. It is also space efficient as it utilizes a single variable for intermediate computation.