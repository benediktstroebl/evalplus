```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum()` function. Note that this function assumes that the input list `lst` is not empty and contains at least one odd index and corresponding even element to meet the criteria of the problem. 
The problem statement mentions "add the even elements that are at odd indices" but the returned result is a single integer representing the sum of odd indexed even numbers, hence the use of `sum()` instead of a concatenated list.