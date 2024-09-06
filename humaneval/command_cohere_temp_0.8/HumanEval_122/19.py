Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i]))<=2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as input. The function operates on the first `k` elements of the array. It iterates through the first `k` elements of the array and checks if the length of the string representation of each element is less than or equal to 2. If so, it adds the integer to the running sum `sum_two_digits`. Finally, the function returns the `sum_two_digits`. 

This code should work as a self-contained Python script to solve the problem you have described. It is adapted from the approach described in the previous message, providing a concise and complete solution to the problem statement. Feel free to test it with any input to verify its functionality!