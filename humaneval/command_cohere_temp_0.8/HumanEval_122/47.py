Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))==1 or len(str(num))==2:
            sum_two_digits += num
    return sum_two_digits
```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums the elements from the first `k` elements of `arr` that have at most 2 digits in its string representation.

The function then loops through the first `k` elements of the array using the variable `i`, converting each element `num` to a string using `str(num)`. It then checks the length of the string representation of each number, either 1 or 2, and adds the number to the running sum if it has 1 or 2 digits. Finally, the function returns the computed sum.

The function is designed to be self-contained and easy to use, and it can be called with specific arrays and values of `k` to calculate the desired sum as needed.