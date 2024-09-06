```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. The problem scenario provided examples for the function's behavior, indicating the desired sum return. 
If the example had included a more complex scenario, such as a list containing multiple arrays or missing values, the function would require additional conditioning to return the desired result. 

Let me know if I can help further, or if you'd like me to make any additional improvements to this function.  Feel free to invite any additional details or specifications regarding the problem you would like me to address.