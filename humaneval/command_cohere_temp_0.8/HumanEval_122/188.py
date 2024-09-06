Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits

# Example usage:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The function `add_elements` takes an array `arr` and an integer `k` as inputs. It iterates through the first `k` elements of the array and checks if the length of the string representation of each element is less than or equal to 2. If so, it adds the value of that element to the `sum_two_digits` variable, which is returned at the end of the function. 

The example usage demonstrates how to call the function with the provided example array and the number of elements to consider (`k`). The output will be as follows:
```bash
Example output: 24
```