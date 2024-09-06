```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for odd numbers that appear in even positions within the list. It utilizes the modulo operator % to determine if a number is odd and uses the index of the number within the list to determine if it appears in an even position. The sum function is then used to add up all the odd numbers in even positions, returning the total as the function's result. The provided example tests, summarized in the comments, demonstrate the function's behavior.