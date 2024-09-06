```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions in the list. To do this, it uses a list comprehension with a conditional statement. The conditional statement `el % 2 == 1 and lst.index(el) % 2 == 0` checks for odd elements in even positions. The `index()` method returns the index of the element, and the modulo operation checks for the evenness of the index. The sum of the elements that satisfy this condition is then returned. This solution adheres to the problem description provided in the markdown code block. 
This solution is efficient because it only iterates over the list once and uses the index checking technique, which is more efficient than manually tracking odd and even positions. It is also concise and easy to understand.