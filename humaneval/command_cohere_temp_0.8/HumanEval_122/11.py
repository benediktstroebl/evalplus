Here's a Python script that contains a function to solve the given problem:
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

This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as input. It then iterates through the first `k` elements of the array, calculates the length of the string representation of each element, and if it has less than or equal to 2 digits, it adds its value to the `sum_two_digits` variable. Finally, it returns the `sum_two_digits` variable.

The example usage demonstrates how to call the function with the provided example array and length `k`, and it prints the calculated sum of elements with at most two digits from the first `k` elements.