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
print(f"The sum of the elements with at most two digits from the first {k} elements is: {result}")
```

This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as input. It then iterates through the first `k` elements of the array, converts each element to a string, and checks if the length of the string is less than or equal to 2. If so, it adds the element to a running sum called `sum_two_digits`. Finally, the function returns the `sum_two_digits`.

The example usage demonstrates how to call the function with a sample array and length parameter and prints the result. You can run this code to see the output which should be:
```
The sum of the elements with at most two digits from the first 4 elements is: 24
```

This solution is efficient and avoids any unnecessary complexity by directly targeting elements that satisfy the condition. It also doesn't require any additional libraries.