Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```
This script defines a function `add_elements` that takes in an array `arr` and an integer `k` as inputs. The function sums up the elements in `arr` that have at most two digits when converted to a string, using a generator expression within the sum function to filter and compute the sum of these elements from the first `k` elements of the array. 

The example usage demonstrates how to call the function with the provided example array and the number of elements to consider (`k`), printing the result to the console. Feel free to add more test cases to ensure the function's correctness for different scenarios.