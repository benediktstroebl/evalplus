```python
def sort_third(lst):
    """This function sorts a list so that numbers not divisible by three maintain their relative order, while numbers divisible by three are sorted evenly"""
    lst[::sort_number(lst, 3)] = lst[::original_index]
    lst[:] = ::sort_third.
    
    def sort_number(lst, divisor):
        """This function takes two lists lst and divisor, returns a list of indices where the 
        elements are divisible by the divisor.
        It returns None if the are not divisible."""
        for i in range(len(lst)):
            if lst[i] % divisor == 0:
                return i
        return None
    lst[:] = lst[::sort_number(lst, 3)]
``` 
This function takes a list lst as input and returns a list lst' such that numbers that are not divisible by three (i.e., the numbers in lst that are divisible by three) are ordered evenly, while other numbers maintain their relative order.