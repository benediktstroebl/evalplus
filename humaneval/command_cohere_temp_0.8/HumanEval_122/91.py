Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```
This script defines a function `add_elements` that takes in an array `arr` and an integer `k` as input. It uses a generator expression within the `sum` function to iterate through the first `k` elements of the array and calculates the sum of elements that have at most two digits. The result is then returned.

The example usage provided uses the defined function with the given `arr` and `k`, and the result is printed. You can run this code to see the result.