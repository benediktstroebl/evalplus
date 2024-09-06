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

The code defines a function `add_elements` that takes in an array `arr` and an integer `k`. It iterates through the first `k` elements of the array, and if the length of the string representation of an element is less than or equal to 2, it adds that element to the `sum_two_digits` variable. Finally, it returns the `sum_two_digits`.

The example usage demonstrates how to call the function with the provided example array and the number of elements to consider (`k`). The output will be as follows:
```bash
Example output: 24
```

This solution is self-contained and can be executed directly to produce the desired results. Keep in mind that you might encounter some constraints when working with large datasets for real-world code challenges. So, it's essential to optimize the code for actual applications. However, for this particular example, the provided solution is efficient and straightforward.