```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even numbers from the list that appear at odd indices number of the list and sums them up. To do this, it utilizes a list comprehension that traverses each element in the list using the enumerate function, which also gives the index of each element. If the index is odd (i.e., divisible by 1 but not by 2) and the element is even, it adds it to the even_odd list. Finally, it returns the sum of the elements in even_odd.