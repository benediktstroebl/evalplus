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
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums the elements in the first `k` entries of `arr` that have either 1 or 2 digits. It does so by iterating through the first `k` elements of `arr` and adding the elements that have 1 or 2 digits to the `sum_two_digits` variable. Finally, it returns the variable `sum_two_digits`. 

This should address your prompt and provide a solution to the specified problem in a self-contained Python script. Let me know if you would like me to explain any part of the script in more detail. I can also provide additional variations or insights related to this solution.