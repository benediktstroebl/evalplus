```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It employs a list comprehension to traverse each element el in the input list. For each element, it checks if the element is odd (el % 2 == 1) and whether it appears in an even-position (determined by lst.index(el) % 2 == 0). If both conditions are met, the element is included in the sum, and the total is returned. Notably, the function directly inherits the examples provided in the problem statement. 
This solution is efficient because it uses Python's built-in index() function for quick positioning of elements, and the sum() function for adding odd elements in even positions. The code has a performance complexity of O(n), where n is the number of elements in the input list.