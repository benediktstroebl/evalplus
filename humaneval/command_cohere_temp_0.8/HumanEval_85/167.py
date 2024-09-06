```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add'. This function takes a list as input and calculates the sum of all even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the index of the element is odd and the element is even, it adds the element to the 'even_odd' list. Finally, it returns the sum of the elements in 'even_odd', which represents the desired result.