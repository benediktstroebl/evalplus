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
print(f"Example output: {result}")
```

The code defines a function `add_elements` that takes in an array `arr` and an integer `k` as input and calculates the sum of elements in the array that have at most two digits. The function then loops through the first `k` elements of the array and adds the elements that have less than or equal to 2-digit numbers to the `sum_two_digits` variable. Finally, the function returns the `sum_two_digits` variable.

The example usage demonstrates how to call the function with the provided example array and length, and the printed output correctly shows the sum of elements that have at most two digits from the first 4 elements of the array, which is 24 in this case. 

This approach efficiently solves the problem in a self-contained manner.