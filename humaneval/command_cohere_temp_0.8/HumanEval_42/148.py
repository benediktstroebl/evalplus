```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
``` 

This Python script defines a function called `incr_list`. This function takes a list l as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing each element. 

Here's an example of how you can use this function:
```python
my_list = [1, 2, 3, 4, 5]
result = incr_list(my_list)
print(result)  # Output: [2, 3, 4, 5, 6]
``` 

This will create a new list `result` with each element from `my_list` incremented by 1. 

The function's behavior is demonstrated in the provided markdown code block, showcasing its capability to correctly increment each element of the list. 
The incr_list function is both concise and efficient, reflecting the best practices of Python scripting.