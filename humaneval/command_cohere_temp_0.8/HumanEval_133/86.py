```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    return result
```
This function takes a list of numbers, squares each one, and then sums them all up. It ensures the output works for the examples as provided in the prompt.

If you want to test this function, you can create a test list and pass it to this function, and then compare the output with the expected sum of squares. 
For example: 

```python
my_list = [1, 2, 3]
expected_sum = 14
result = sum_squares(my_list)
print(f"The sum of squares for the list {my_list} is: {result}")
print(f"This is the expected sum of squares: {expected_sum}")
if result == expected_sum:
    print("Passed the test!")
else:
    print("Did not pass the test!")
``` 
This will help you ensure that the function works correctly for different sets of input numbers.