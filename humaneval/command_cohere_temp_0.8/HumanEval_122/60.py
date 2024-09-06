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
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums the elements in the first `k` entries of `arr` that have either 1 or 2 digits. It does this by initializing a variable `sum_two_digits` to 0 and looping through the first `k` elements of `arr`. For each element, it checks whether the length of its string representation is either 1 or 2, and if so, it adds it to the sum. Finally, it returns the accumulated sum of these elements. 

The function successfully passes the test case provided in the prompt, as shown by the following markdown code block:
```python
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))
>>> 24
```