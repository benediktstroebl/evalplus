```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices within the list and then calculates their sum. To achieve this, it employs a list comprehension, iterating through each element and index of the input list. If the index is odd (i.e., divisible by 1 but not by 2) and the element is even, it adds the element to the 'even_odd' list. The function then returns the sum of the elements in the 'even_odd' list, providing the total of all even integers present at odd indices in the original list. 

The function efficiently solves the problem statement without modifying the original list, ensuring the integrity of the input data, and delivering the desired result through a concise and optimized approach.

This approach uses a list comprehension to find even elements at odd indices. It does this without modifying the original list, which prevents side effects and maintains the list's integrity for further analysis if needed. The use of the `enumerate` function allows for indexing and element checking in a single loop, improving efficiency and readability.