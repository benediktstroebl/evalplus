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

The function `add_elements` takes an array `arr` and an integer `k` as input, and calculates the sum of elements from the first `k` elements of `arr` that have at most two digits. It iterates through the array and adds elements with lengths less than or equal to 2 to the `sum_two_digits` variable. Finally, the function returns the calculated sum.

The example usage demonstrates how to call the function with the given example array and the number of elements to consider, and prints the result accordingly.