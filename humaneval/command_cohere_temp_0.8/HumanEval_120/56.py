Here's a Python script that contains a function to solve the given problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Example usage
input_arr = [-3, -4, 5]
input_k = 3

result = maximum(input_arr, input_k)
print(result)  # Output: [-4, -3, 5]

```
This script will output `[-4, -3, 5]` which is the maximum integer value within the array that is encountered k times. We sort the array and return the first `k` elements to achieve this.