Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for positive values, and returns a new list that includes only the positive numbers from the input list `l`. 
The script passes the tests provided in the prompt:
```python
>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
``` 
As demonstrated, the output is consistent with the expected results in the original problem statement. In this case, the function get_positive efficiently and succinctly isolates the positive values from the given list, demonstrating the list comprehension's expressive power for such filtering tasks. 
If you would like to examine or modify the function's behavior to accommodate other scenarios, the script is readily accessible for your exploration. 
Feel free to induce further tests to verify its function under diverse situations, confirming its adaptability as a robust solution for filtering positive numbers among a list of numbers.  enjoy!