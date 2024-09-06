Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))==1: 
            sum_two_digits += num
        elif len(str(num))==2: 
            sum_two_digits += num
    return sum_two_digits

# Example usage:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f'Example output: {result}')

```
This script defines a function `add_elements` that takes in an array `arr` and an integer `k` as input, and calculates the sum of elements in the first `k` elements of `arr` that have at most two digits.

The script includes an example usage with the given example in the prompt and runs without issues. Feel free to modify the test cases according to your requirements! Let me know if you need any further modifications.