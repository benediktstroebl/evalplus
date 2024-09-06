Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))<=2:
            sum_two_digits += num  
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")
```

The script defines a function `add_elements` that takes in an array `arr` and an integer `k` as inputs. It iterates through the first `k` elements of the array, and for each element, it checks if the length of the string representation of the number is less than or equal to 2. If so, it adds the number to the `sum_two_digits` variable, which is used to store the sum of the elements that satisfy this condition. Finally, the function returns `sum_two_digits`.

The example usage is also provided in the script, where the function is called with the given example array `arr` and length `k`, and the output is printed.