```python
def sort_even(lst):
    """This function sorts even numbers in a list while preserving the relative order of odd numbers.
    >>> sorted(lst,key=lambda x: not_even(x))
    lst[:] = [x for x in lst if not_even(x)]
    return sorted(lst)

def not_even(x):
    return x % 2 == 0

# Test the function
# [1,2,3] -> [1,2,3]
# [5,6,3,4] -> [3,6,5,4]
# [8,9,4,7] -> [8,9,4,7]
```
This Python script defines a function `sort_even` that takes a list as input and returns a sorted list of numbers. The function works by first checking if each number in the input list is even or odd, and then using the `sorted` function with a custom key that uses the `not_even` function to sort the even numbers. The function also uses the other numbers in the list to maintain their relative order.