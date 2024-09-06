```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add'. This function accepts a list of numbers as an input. It aims to compute the sum of all even numbers within the list that appear at odd indices. To achieve this, it employs a list comprehension, which iterates through each element in the input list. For each element, it checks two conditions: first, whether the current index is odd (i.e., not divisible by 2), and second, whether the element itself is even (also divisible by 2). If both conditions are satisfied, the element is included in the 'even_odd' list. Finally, the function sums up the elements within the 'even_odd' list and returns the result, providing the total of all even numbers at odd indices in the input list.