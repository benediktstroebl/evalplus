Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This function iterates through the first `k` elements of the `arr` array and checks if the length of the string representation of its elements is less than or equal to 2. If so, it accumulates their sum in the `sum_two_digits` variable, which is then returned at the end of the function.

Here is an example of an input/output scenario that would demonstrate the function's functionality: 
**Example:**
```
Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
Output: 24
```
In this instance, the array contains the following values: [111, 21, 3, 4000, 5, 6, 7, 8, 9]. The function has been called with the array and the value of `k` set to 4. The function will return 24, which is the sum of the first four elements of the array whose representations have one digit: 21+3.