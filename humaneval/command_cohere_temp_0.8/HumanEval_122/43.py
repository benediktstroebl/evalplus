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
print(f"The sum of elements with at most two digits from the first {k} elements is: {result}")
```

The script provides a function called `add_elements` that takes in an array `arr` and an integer `k` as input. This function sums up the elements in `arr` that have at most 2 digits. It does this by iterating through the first `k` elements of the array and checks if the length of the string representation of each number is less than or equal to 2. The example usage demonstrates how to call the function with a sample array and a specific value of `k`, printing the result accordingly.