```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and (len(lst) - x + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in the list that are also in even positions. The conditional checks for divisibility by 2 and oddness are done using the modulo operator %. The list comprehension iterates through each element in the input list, and the sum function adds up the values that meet the specified conditions. The result is the total sum of odd numbers in even positions within the list, which is then returned by the function.