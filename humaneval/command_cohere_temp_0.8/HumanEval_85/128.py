```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the index of the element is odd and the element is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, which effectively captures the desired even elements at odd indices, and prints the result.