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

The code defines a function `add_elements` that takes in an array `arr` and an integer `k` as inputs. It iterates through the first `k` elements of the array, and for each element, it checks if the length of the string representation of the element is less than or equal to 2. If it is, it adds the element to the `sum_two_digits` variable. Finally, it returns the `sum_two_digits`. 

The example usage is added to demonstrate how to call the function with a sample array and length. The output will show the sum of elements with at most two digits from the first 4 elements of the array.  This code solves the problem and should produce the correct output. Feel free to test it with different inputs and verify the results! Let me know if you have any other questions or if you'd like me to assist with anything else.