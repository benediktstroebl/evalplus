Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))==1: 
            sum_two_digits += num
        elif len(str(num))==2: 
            sum_two_digits += num
    return sum_two_digits
```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`, and returns the sum of the elements in the first `k` elements of `arr` that have at most two digits.

The function uses a for loop to iterate through the first `k` elements of the array `arr`. For each element, it checks the number of digits in the element's string representation using the `len()` function.

If the element has one digit, it is added to a running sum `sum_two_digits`, which counts the sum of all elements with one or two digits. If the element has two digits, it is also added to `sum_two_digits`.

After looping through all elements, the function returns the `sum_two_digits`.

The script solves the problem and can be used as a standalone function to calculate the desired sum for any given input array and value of `k`.