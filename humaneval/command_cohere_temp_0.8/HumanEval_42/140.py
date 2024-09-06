Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The result is then returned as the output. 
The script does not have any external dependencies and can be run standalone. It is modular and can be used in other scripts as needed. It is also concise and readable, expressing the logic succinctly.