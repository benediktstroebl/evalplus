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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

This script defines a function `add_elements` that takes an array `arr` and an integer `k` as input, it initializes a variable `sum_two_digits` to 0 and iterates through the first `k` elements of the array. It adds the elements to the sum if their string representation has <= 2 digits (i.e., they are less than 100). Finally, it returns the computed sum. 

The example usage demonstrates how to call this function with the provided array and K value and prints the result.