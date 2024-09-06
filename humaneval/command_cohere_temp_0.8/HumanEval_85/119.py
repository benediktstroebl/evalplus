```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of integers as input. It aims to collect the even integers present at odd indices of the list using a list comprehension. The collected even integers are then summed using the 'sum()' function, providing the total of these even elements at odd indices. The function returns this sum. 

This solution fulfills the problem statement and corresponds to the test cases provided earlier. 
Would you like to know more about the code or anything else related to the problem? Let's dive deeper or explore other topics if you have any specific interests.  feel free to ask questions or express your concerns, and I'll be glad to accommodate accordingly.