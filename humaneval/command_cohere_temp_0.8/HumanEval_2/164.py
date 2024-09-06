```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the desired decimal part of the number. 

Here is a simple test case to confirm the correct functionality of the function:
```python
truncate_number(3.5)
# Expected output: 0.5
``` 
You can confirm that the above code output is `0.5`. 

Let me know if you would like to have the test case formatted in markdown code block or if you would like to solve another problem you might have.