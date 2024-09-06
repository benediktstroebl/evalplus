```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of integers as input. It aims to retrieve even integers located at odd indices within the list and then calculates their sum. To achieve this, it employs a list comprehension, iterating through each element's index in the input list using the enumerate() function. When the index is odd (i % 2 == 1) and the element is even (el % 2 == 0), the element is added to the even_odd list. The function then returns the sum of the even integers located at odd indices in the list, resulting in the desired output.