```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element el in lst. Within the list comprehension, two conditions are checked: el % 2 == 1 checks if the element is odd, and lst.index(el) % 2 == 0 checks if the element's index is even. The index() function is used to determine the index of the current element. The sum() function then calculates the sum of the elements that satisfy both conditions. This odd-in-even-positions sum is returned as the function's result. 

The script provides an efficient and concise solution to the problem statement, directly returning the desired sum as specified in the function's definition.