```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The Python script defines a function `largest_smallest_integers` that solves the problem as described in the prompt. It iterates through the list, identifying the largest negative and smallest positive integers, or `None` if none are found. 

This responds to the request and provides an effective solution, enabling users to find the desired largest and smallest numbers in a list of integers efficiently. 

For better code organization and readability, I've added variable names (`negative` and `positive`) to track the largest negative and smallest positive integers, respectively. This approach enhances clarity and maintains a consistent style, making the code easier to understand and maintain.