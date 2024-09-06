```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even integers present at odd indices of the list and calculate their sum. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the index of the element is odd and the element is even, it adds it to the 'even_odd' list. Finally, the function returns the sum of the collected even integers, providing a quick way to solve this specific problem.