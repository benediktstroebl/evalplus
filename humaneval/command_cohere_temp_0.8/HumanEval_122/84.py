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
This function iterates through the first k elements of the input array `arr`. It converts each element to a string, checks its length, and adds those with a length of 1 or 2 to the `sum_two_digits` variable. Finally, it returns the calculated sum. 

Note that this code assumes the existence of a separate unit test file with appropriate test cases, as it does not include test cases within the script. Make sure to include tests in your solution to verify the functionality of the code.