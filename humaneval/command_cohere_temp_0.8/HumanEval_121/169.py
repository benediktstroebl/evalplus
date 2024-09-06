```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It employs a list comprehension to iterate through each element el in the input list. For each element, it checks two conditions:
1. Whether the element is odd (i.e., its remainder when divided by 2 is equal to 1).
2. Whether the element appears in an even position within the list (i.e., its index modulo 2 equals 0).

If both conditions are true for a specific element, it is included in the sum calculated by the function. The result is the total of odd elements that occupy even positions within the list, as described in the problem statement.