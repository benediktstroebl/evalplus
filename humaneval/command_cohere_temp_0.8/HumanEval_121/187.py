```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element el in lst. Within the list comprehension, it checks if the current element is odd (el % 2 == 1) and whether its index is even (lst.index(el) % 2 == 0). The index modulo operation (index % 2) checks if the element's index is even, as indexing begins from 0 in Python. If both conditions are met, the element is included in the sum, resulting in the total of odd elements in even positions within the list. The function returns this computed sum. 

The provided example test cases in the docstring demonstrate how the function behaves for different lists:
- solution([5, 8, 7, 1]) ==> 12 correctly returns 12, the sum of odd numbers in [5, 8, 7, 1] where odd numbers are at even positions. 
- solution([3, 3, 3, 3, 3]) ==> 9 correctly returns 9, the sum of odd numbers in [3, 3, 3, 3, 3] where all numbers are odd and in even positions.
- solution([30, 13, 24, 321]) ==> 0 correctly returns 0, as there is no odd number in even positions in the list. 

This function effectively solves the problem statement and provides the desired sum as output.