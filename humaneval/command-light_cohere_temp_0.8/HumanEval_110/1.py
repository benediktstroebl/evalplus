```python
def exchange(lst1, lst2):
    """
    Determine if it is possible to make lst1 an list of only even numbers by exchanging elements with lst2, 
    and return "YES" if successful, otherwise "NO".
    """
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] & 1 != lst2[i] & 1:
            return "NO"
    return "YES"

# Example usage:
exchange([1, 2, 3, 4], [1, 2, 3, 4])  # Output: YES
exchange([1, 2, 3, 4], [1, 5, 3, 4])  # Output: NO
```
The function exchange in this code takes two lists lst1 and lst2 as input. It checks whether it particular list can be converted into a list of only even numbers, then it returns "YES". If not lists have different lengths or any element in lst1 does not match the corresponding element in lst2, it returns "NO". If the lists match, it returns "YES".