```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and creates a pile of stones as described in the problem statement. It starts with a base level of n stones and iteratively calculates the next level's stone count (odd if the previous count was odd, even if the previous count was even), adding it to the pile. This process continues until the pile contains n+1 levels. The final result is a list of stone counts for each level. 

The code is encapsulated in a function, making it testable and reusable. It also adheres to Python's style guidelines, ensuring readability and maintainability.