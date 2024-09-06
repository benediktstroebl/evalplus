```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the `sum` function to add these numbers. 

Here is a sample usage of the function adding the even elements at odd indices of the list `[4, 2, 6, 7]` to yield `2`:
```python
add([4, 2, 6, 7]) # 2
``` 
This problem can be solved in different ways, and this is just one example, 
if you'd like to discuss further alternatives, feel free to ask!