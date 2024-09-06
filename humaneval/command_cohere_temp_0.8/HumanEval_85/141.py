```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

The test cases allow us to verify the correctness of the implemented function. 

If needed, I can assist with detailing the unit tests, or providing insight on how the function works. Let me know, and I'll be happy to help!