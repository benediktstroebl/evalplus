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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

The function `add_elements` takes an array `arr` and an integer `k` as input, and iterates through the first `k` elements of the array. It converts each element to a string and checks if the length of the string is less than or equal to 2. If so, it adds that element to the sum `sum_two_digits`. Finally, the function returns `sum_two_digits`.

The example usage demonstrates how to call the function with the given array and value of `k`, and prints the result.