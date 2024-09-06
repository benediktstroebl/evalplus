Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The code defines a function `add_elements` that takes in an array `arr` and an integer `k` as inputs. It iterates through the first `k` elements of the array and checks if the length of the string representation of the element is less than or equal to 2. If so, it adds the element to the `sum_two_digits` variable.

The script also includes an example usage of the function with a commented output statement. You can uncomment the print statement to see the result of the example given in the problem statement. Make sure to replace the `arr` and `k` variables with the values you want to test.