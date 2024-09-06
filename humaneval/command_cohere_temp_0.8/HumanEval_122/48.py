Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i]))<=2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This script uses a `for` loop to iterate through the first `k` elements of the `arr` list. It determines whether the length of the string representation of each element is less than or equal to 2. If so, it adds the element to the `sum_two_digits` variable, which stores the sum of elements that have at most two digits. Finally, it returns the sum_two_digits variable.