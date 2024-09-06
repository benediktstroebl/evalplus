```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
``` 

This function uses a list comprehension to filter even integers at odd indices from the input list `lst`. These are stored in the `even_odd` list, and their sum is returned as the function's result. 

Would you like to know more about the approach or anything else related to the problem?
Let me know if you'd like to see more examples or explore other concepts.