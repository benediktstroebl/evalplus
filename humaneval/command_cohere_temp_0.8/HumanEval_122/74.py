Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This function `add_elements(arr, k)` takes an array `arr` and an integer `k` as input, and calculates the sum of elements in the first `k` entries of `arr` that have at most two digits. The loop iterates through the first `k` elements of the array, and for each element, it checks if the length of its string representation is less than or equal to 2. If so, it adds that element to the running total `sum_two_digits`. The function returns the final total, which is the sum of elements with at most two digits from the first `k` elements of `arr`. 

The function relies on a simple loop and string length check to solve the problem, making it efficient and adaptable to different types of integer inputs.