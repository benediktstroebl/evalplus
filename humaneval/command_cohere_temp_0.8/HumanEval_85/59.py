```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the input list. To achieve this, it employs a list comprehension, iterating through each element and index in the input list. If the current index is odd and the element is even, it adds the element to the 'even_odd' list. The final result is the sum of the odd index even elements, efficiently solved through the list comprehension. 

The function works correctly and follows the expected behavior, as confirmed by tests. It returns the expected sum of even elements at odd indices in the given examples, making it a valuable tool for solving this specific problem.  It is essential to ensure that the input list contains at least one even element at an odd index to yield a non-zero result.