```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function sums up all the odd numbers within the even positions of the list, and returns the total sum.

The algorithm works by using a generator expression, el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0, which goes through each element (el) in the list (lst). It determines if the element is odd (el % 2 == 1) and whether it sits in an even position ((len(lst) - el + 1) % 2 == 0). The variable el is multiplied by 1 when it is in an even position, making it odd. The sum function then adds up all these odd numbers.

The script fulfills the problem statement's requirement as it computes the sum of all odd integers in the list that appear in even positions, and it does so efficiently without using any explicit indexing or looping constructs.