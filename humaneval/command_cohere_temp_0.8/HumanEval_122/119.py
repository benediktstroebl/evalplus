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

The script provides a function `add_elements` that takes in an array `arr` and an integer `k` as input. It iterates through the first `k` elements of the array, and for each element, it checks if the length of the string representation of the element is less than or equal to 2. If so, it adds the element to the `sum_two_digits` variable. Finally, the function returns the `sum_two_digits` variable. The example usage demonstrates how to call the function with a sample array and length `k`, and it prints the result accordingly.