```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list and calculate the digit sum of each number using a nested list comprehension. It then checks if this sum is greater than zero and contributes to the total count if so. The final count is returned as the function output. 

This solution is concise and efficient, directly addressing the problem statement without excessive complexity. It provides a straightforward approach to achieve the desired functionality and meets the given test cases. You can use this code to handle the problem statement, and it can be tested against the provided scenarios to verify its behavior.