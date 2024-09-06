```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```

The code uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. The solution is efficient with a time complexity of O(n) where n is the length of the list `lst`. 

For smaller lists, it may be more intuitive to solve this problem using the following approach:
```python
def add(lst):
    even_odd = []
    for i, num in enumerate(lst):
        if i % 2 == 1 and num % 2 == 0:
            even_odd.append(num)
    return sum(even_odd)
```

Feel free to experiment with different approaches to find the most optimal solution for your specific list size! Let me know if you'd like further refinement to the code or if you have any other questions at all.