```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To do this, it employs a list comprehension with a generator expression, checking for elements that meet the condition of being odd and located in even positions. The sum of these qualifying elements is then returned, as indicated in the Markdown code block provided.