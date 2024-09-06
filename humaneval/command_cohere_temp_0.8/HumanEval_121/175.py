```python
def solution(lst):
    return sum(x for x in lst if x % 2 and (len(lst) - x + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. It calculates the sum of odd numbers within the even positions of the list. To achieve this, it uses a generator expression, filtering out elements that are odd and positioned at even intervals within the list. The result is the sum of these filtered numbers. The function is designed to work for any valid input list of integers and returns the desired sum, as specified in the problem description.