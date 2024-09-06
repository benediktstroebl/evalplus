```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as input and aims to calculate the sum of even integers present at odd indices in the list. To achieve this, it uses a list comprehension, iterating through each element in the input list. If the index of the element is odd (i%2==1) and the element is even (el%2==0), it includes the element in the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, which represents the desired sum of even integers at odd indices in the input list.