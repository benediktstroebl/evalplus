Here's a self-contained Python script that defines a function **filter_integers** solving the given markdown code problem:
```python
from typing import List

def filter_integers(values:
    inp_values = values.cast(List(values)
    return [int(x) for x in inp_values if x.isinstance(int)])
```
The above Python script defines a function **filter_integers** that takes a list of values as a parameter and returns a new list that contains only the integers from the input list. It uses the Python's **isinstance** operator to check if the element is an integer and then cast the element to an integer using the **int()** function. The function also uses the Python's **List** function and the **cast** operator to create a new list that contains only the integers from the input list.