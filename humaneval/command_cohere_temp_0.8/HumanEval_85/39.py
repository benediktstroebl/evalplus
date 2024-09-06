```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
``` 

This function uses a list comprehension to filter even integers at odd indices from the input list `lst`. These integers are then added together using the `sum` function and returned. 

Would you like to know more about the approach or any specific part of the code? 

Let me know if you'd like to generate further examples or clarify any other concepts within the problem!