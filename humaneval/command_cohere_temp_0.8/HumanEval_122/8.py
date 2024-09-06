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
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k` as inputs. The function sums up the elements from the first `k` elements of `arr` that have at most two digits.

The script then provides an example usage of this function with the given example inputs (`arr` and `k`), and the corresponding output is printed. 

Note that this code assumes that the constraints given in the prompt are followed, i.e., the length of the input array is between 1 and 100, and the value of 'k' is between 1 and the length of the input array.