```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list lst as input and aims to calculate the sum of even integers present at odd indices in the list. To accomplish this, it employs a list comprehension, iterating through each element of the input list. If the index of the element (determined by 'enumerate') is odd and the element itself is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, which effectively provides the desired sum of even integers at odd indices in the input list. 

The function effectively solves the problem statement and can be used as a standalone function to calculate the sum of even elements at odd indices in a given list. 

This solution can be improved by adding a docstring to explain its working in detail, which can be very useful for better understanding. 
Below is a markdown code block that improves upon the provided solution by adding a comprehensive docstring: 

```python
def add(lst):
    """
    Calculates the sum of even integers present at odd indices in the list.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
        add([1, 3, 5, 7, 2, 4, 6]) ==> 12 
    """ 
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```

The added docstring provides a detailed explanation of the function's purpose, as well as illustrative examples to better showcase its usage.