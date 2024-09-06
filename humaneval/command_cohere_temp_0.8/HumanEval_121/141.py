```python
def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and lst.index(num) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, checking if each number in the input list is odd and if its index is even. The `index()` method returns the index of the element within the list, and the `%` operator checks if the index is even (multiple of 2). The sum of odd numbers that satisfy both conditions is then returned as the result.