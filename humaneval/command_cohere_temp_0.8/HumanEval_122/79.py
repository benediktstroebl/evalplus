Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num)) <= 2: 
            sum_two_digits += num
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The function `add_elements` takes an array `arr` and an integer `k` as inputs. It iterates through the first `k` elements of the array, and for each element, it checks if the length of the string representation of the number is less than or equal to 2. If so, it adds the number to the `sum_two_digits` variable, which is returned at the end of the function. 

The example usage is provided in the code with the desired output formatted inside a Markdown code block. Feel free to edit the test input and adjust the expected output accordingly. Let me know if you need any further clarification or have additional questions!