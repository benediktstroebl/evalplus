```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that the function assumes that the list contains only integers, as this is the common case for lists of numbers; however, it may be desirable to introduce a type constraint and corresponding test to ensure this property. 

Let me know if you'd like to test this function using a sample list, or if you'd like any other modifications to be made to the script.