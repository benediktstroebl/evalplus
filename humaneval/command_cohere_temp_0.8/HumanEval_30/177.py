Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to retrieve positive numbers from the input list. The `if` statement within the list comprehension performs the filtering process. The returned list `[x for x in l if x > 0]` only contains elements that meet the condition `x > 0`, effectively filtering out all negative numbers. 
The function thoroughly solves the problem of filtering out only positive numbers from the input list, providing a concise and efficient solution.