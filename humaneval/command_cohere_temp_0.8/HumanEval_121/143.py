```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for odd numbers that appear in even positions within the list. The expression lst.index(el) returns the index of the element el in the list lst. Note that el % 2 == 1 checks if the element el is odd, and lst.index(el) % 2 == 0 checks if the element is in an even position in the list. The function returns the sum of all the odd numbers that satisfy these conditions, which is the desired output.