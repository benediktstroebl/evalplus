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

This script defines a function `add_elements` that takes in an array `arr` and an integer `k` as input. It iterates through the first `k` elements of the array and checks if the length of the string representation of each element is less than or equal to 2. The sum of the elements meeting this condition is then returned.

The example usage demonstrates how to call the function with the provided example array and k value and print the result.