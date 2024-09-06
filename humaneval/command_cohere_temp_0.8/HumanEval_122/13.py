Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))==1 or len(str(num))==2:
            sum_two_digits += num
    return sum_two_digits

# Example usage:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"The sum of elements with at most two digits from the first {k} elements is: {result}")
```

This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as input, and calculates the sum of elements in the first `k` array elements that have either one or two digits. The script then provides an example usage of this function and prints the result.