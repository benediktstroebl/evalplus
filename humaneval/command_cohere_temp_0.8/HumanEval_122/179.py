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

This script defines a function `add_elements` that takes an array `arr` and an integer `k` as input, and calculates the sum of elements in `arr` that have at most two digits when converted to a string. The function iterates through the first `k` elements of the array, and if the length of the string representation of the element is less than or equal to 2, it adds the element to the `sum_two_digits` variable. Finally, the function returns the calculated sum.

The example usage demonstrates how to call the function with the provided array and value of `k`, and prints the result. The output will be:
```bash
The sum of elements with at most two digits from the first 4 elements is: 24
```

This solution is efficient and directly calculates the sum of elements with at most two digits, without any extra complexity. It is concise and easy to understand, fulfilling the requirement of a self-contained solution.