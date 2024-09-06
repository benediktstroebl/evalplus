```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions in the list. To accomplish this, it employs a list comprehension with a conditional statement. The sum function is then used to add up the values that satisfy this condition, resulting in the total of odd elements in even positions. The script returns this computed sum. 

The function works as follows:
- It takes a list called `lst` as input.
- It uses a list comprehension to iterate over each element `el` in the input list `lst`.
- The comprehension employs a conditional statement `el % 2 == 1 and lst.index(el) % 2 == 0` to filter odd elements in even positions. `el % 2 == 1` checks if the current element is odd, and `lst.index(el) % 2 == 0` checks if the index of the current element is even. The `index()` method returns the index of the element in the list.
- The `sum()` function adds up the values of all elements that satisfy the condition, resulting in the total of odd elements in even positions.
- Finally, the computed sum is returned as the output of the function.