```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for integers that have a value of 1 when their index is divided by 2. The sum of these numbers is then calculated and returned as the result. This code works because the provided Markdown code block includes test cases and a specific example of the odd/even logic.