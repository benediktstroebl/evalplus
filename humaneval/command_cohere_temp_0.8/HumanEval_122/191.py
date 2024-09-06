Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i]))<=2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This function iterates through the first `k` elements of the `arr` array and checks if the length of the string representation of its elements is less than or equal to 2. If so, it accumulates their sum in the `sum_two_digits` variable, which is then returned.

This solution follows the specified constraints and should be able to pass the respective tests. Feel free to ask any questions or provide any additional feedback!