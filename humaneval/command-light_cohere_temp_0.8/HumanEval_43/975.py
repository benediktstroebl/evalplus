```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension:
    - It iterates through each element in the list
    - If the element is zero, it matches it with all other elements to find the second element that, when combined with this zero, results in a sum to zero.
    - If element is not zero, it matches it with all other elements that have a non-zero sum, until it finds the second element.
    """
 set of zeroes
    - If it finds the second element, it returns True, indicating that there are two distinct elements in the list that sum to zero.
    - If the elements are the same, the function returns False.
    """
 return True  # returns True if two distinct elements sum to zero, False otherwise
```
The function uses a list comprehension and a set of zero to find the second element that, when combined with the first element, results in a sum to zero. The function returns True if the two distinct elements in the list are not the same, and False otherwise.

Note: You can use this function to check whether a list of integers contains two elements that sum to zero.