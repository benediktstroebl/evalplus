Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))<=2:
            sum_two_digits += num
    return sum_two_digits

# Example usage:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f'Example output: {result}')
```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums up the elements from the first `k` elements of `arr` that have at most two digits. It does this by iterating through the first `k` elements of the array, converting each element to a string, and checking if the length of the string is less than or equal to 2. If so, it adds that element to the `sum_two_digits` variable, which is initialized to 0. Finally, it returns the `sum_two_digits` variable.

The example usage provides an array `arr` and an integer `k` to the function and prints out the sum of elements with at most two digits from the first `k` elements.