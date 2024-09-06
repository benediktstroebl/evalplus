Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This function `add_elements(arr, k)` takes an array `arr` and an integer `k` as input, and calculates the sum of elements in the first `k` entries of `arr` that have at most two digits. The loop iterates through the first `k` elements of the array, and for each element, it checks if the length of its string representation is less than or equal to 2. If it meets these conditions, the value is added to the `sum_two_digits` variable, which is returned at the end as the final result. 
The function efficiently solves the problem and returns the required sum.