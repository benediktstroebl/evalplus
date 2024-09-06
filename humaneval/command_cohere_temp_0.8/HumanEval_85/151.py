```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices within the list and then calculates their sum. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the current index is odd and the element is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the collected even integers, providing a convenient way to obtain the desired result.