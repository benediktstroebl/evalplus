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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

The function `add_elements` processes the first `k` elements of the `arr` array. It iterates through these elements and calculates the sum of those whose string representation has at most two digits. The result is then returned as the sum of these selected elements. 

The example usage demonstrates how to call the function with the provided input and print the result. Adjust the values of `arr` and `k` as needed.