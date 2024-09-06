```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices within the list and then calculates their sum. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the current element is even and its index is odd (i.e., index % 2 == 1), it gets included in the 'even_odd' list. Finally, the function returns the sum of the oddly positioned even integers within the 'even_odd' list. 

The function elegantly solves the problem statement without needing any additional variables, making it concise and effective. It provides a straightforward way to find the sum of even elements at odd positions within a given list of integers.