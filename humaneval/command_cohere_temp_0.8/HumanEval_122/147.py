Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i]))<=2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This function iterates through the first `k` elements of the `arr` array and checks if the length of the string representation of its elements is less than or equal to 2. If so, it accumulates their sums in the `sum_two_digits` variable, which is then returned at the end.

This solution adheres to the specified constraints, and should function correctly given those constraints. Let me know if you'd like me to explain any part of the code further.