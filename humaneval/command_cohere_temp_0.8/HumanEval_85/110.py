```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as an input. It aims to collect the even integers present at odd indices of the list and calculates their sum. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the current element is even and it appears at an odd-indexed position (checked using the modulo operator), it gets included in the 'even_odd' list. Finally, the function returns the sum of the oddly-indexed even numbers in the provided list, representing the desired result.