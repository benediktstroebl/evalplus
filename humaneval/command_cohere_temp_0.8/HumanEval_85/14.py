```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as an input. It aims to collect the even numbers present at odd indices of the list and calculates their sum. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the current element is even and its index is odd (i.e., divisible by 1 but not by 2), it adds it to the 'even_odd' list. Finally, the function returns the sum of the collected even numbers, providing a solution to the problem statement.