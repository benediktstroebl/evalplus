```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element (el) of the input list (lst) using the enumerate function. The comprehension checks if the current index (i) is odd (1-indexed) and the element is even (el % 2 == 0), in such cases, the even elements are collected in the even_odd list. Finally, the function returns the sum of the even numbers collected in even_odd. Note that this approach has a time complexity of O(n), where n is the length of the input list, as it iterates through each element once.