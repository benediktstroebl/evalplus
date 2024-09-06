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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

The function `add_elements` iterates through the first `k` elements of the `arr` list and accumulates the sum of elements that have a length of at most 2 when converted to a string. The result is then returned. The example usage demonstrates how to call the function with the provided example input and print the result. Make sure to have a `python` interpreter installed. You can paste the code into a Python file and run it or use an online Python interpreter.