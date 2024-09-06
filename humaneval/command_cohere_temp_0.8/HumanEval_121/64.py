```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To do this, it employs a list comprehension that iterates through each element el in the input list. It checks if the element is odd (el % 2 == 1) and whether it appears in an even position (indexed in lst such that lst.index(el) % 2 == 0). If both conditions are met, the element is included in the sum, which is then returned as the function's output.