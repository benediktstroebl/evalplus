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

This script defines a function `add_elements` that takes in an array `arr` and an integer `k` as input. It then iterates through the first `k` elements of the array, calculates the sum of elements that have at most two digits, and returns the sum. The code example shows how to use this function with a specific array and value of `k`, printing the result as described in the problem statement.