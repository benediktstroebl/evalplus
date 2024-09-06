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
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums up the elements in the first `k` elements of `arr` that have at most 2 digits in their decimal representation.

The function then uses a `for` loop to iterate through the first `k` elements of the array `arr`. It then checks the number of digits in the decimal representation of each number using the `len` function to convert it into a string and then into an integer, if the length is 1 or 2, those numbers are added to the sum_two_digits variable. Finally, the function returns the `sum_two_digits` variable. 

This solution adheres to the constraints provided, ensuring that it works for arrays with up to 100 elements and allows for values of k between 1 and the length of the array.