```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. The problem scenario provided a list of integers, and the function computes the sum of even integers appearing at odd positions. This solution is concise and provides an optimal algorithm for the problem.