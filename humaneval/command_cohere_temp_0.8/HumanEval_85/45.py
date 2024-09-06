```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices in the list and calculates their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. If the current index is odd (i.e., divisible by 1) and the element is even (i.e., divisible by 2), it adds the element to the `even_odd` list. The function then returns the sum of the elements in the `even_odd` list. This solution effectively addresses the problem statement and provides the desired summation of even elements at odd indices in the given list.