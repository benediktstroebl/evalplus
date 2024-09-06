```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list and calculate the digit sum of each number using a nested list comprehension. It then checks if this sum is greater than zero and contributes to the total count if so. Finally, it returns this total count. 

You can test this function by calling it with different arrays and comparing the output with the expected results defined in the markdown code block.