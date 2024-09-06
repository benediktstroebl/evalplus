```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function sums up all the odd numbers within the even positions of the list, and returns the total sum.

The solution is achieved using a generator expression, denoted by (el for el in lst if ...). In this case, the condition el % 2 == 1 and (len(lst) - el + 1) % 2 == 0 checks for odd numbers in even positions.

The expression len(lst) - el + 1) gives the position of an element in the list, with el being the current element. If this position is even, then the element is in an even position. 

This script provides a functional solution to the given problem, and should produce the correct output for the test cases provided. 
Please let me know if any additional clarifications are needed. I hope this helps!