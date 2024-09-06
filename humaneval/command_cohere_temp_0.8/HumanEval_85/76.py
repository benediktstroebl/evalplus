```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that this function assumes that the list contains only integers, as the `%` operator is used to determine even or oddness. If the list contains other data types, the function may not return the expected results. 

Let's break down the solution into smaller steps: 
* We want to return the sum of even integers in the list that are located at odd indices. To do this, we use a list comprehension that filters out the relevant elements. 
 * We enumerate the list, and for each element, we check if the index has an odd parity (i% 2 == 1), and the value has an even parity (val % 2 == 0). 
 * If both parities match, the element is added to the even_odd list. 
 * Finally, we return the sum of the elements in the even_odd list. 

This solution is efficiently implemented in a single pass through the list, making it an optimal solution for this problem.