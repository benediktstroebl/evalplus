```python
def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
```
This Python script provides a function called solution(), which takes a list of numbers as input and returns the sum of all odd numbers present in the list that are in even positions. To achieve this, it utilizes a generator expression, created with the help of the sum() function, which intelligently filters out odd numbers and calculates the sum of these numbers. The resulting output is then returned to the user.