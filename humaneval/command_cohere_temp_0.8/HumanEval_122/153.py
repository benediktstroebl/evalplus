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

The function `add_elements` iterates through the first `k` elements of the `arr` list, and for each element, it checks the length of its string representation. If it has a single digit, it's added to the sum; if it has two digits, it's also added to the sum. The example usage and output are also provided, where the sum of elements with at most two digits from the first 4 elements of the array is 24 (from elements '21' and '3').