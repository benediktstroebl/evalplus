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

The function `add_elements` takes an array `arr` and an integer `k` as input, and calculates the sum of elements from the first `k` elements that have at most two digits. It iterates through the array and accumulates the sum of elements that meet this criteria in the `sum_two_digits` variable. Finally, it returns the computed sum.

The example usage demonstrates how to call the function with the provided array and the number of elements to consider, and prints the result accordingly. Make sure to have the `arr` and `k` variables defined before calling the function with the appropriate values.