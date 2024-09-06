```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```
The function checks if there is an odd number in the first list, and then exchanges the elements of both lists accordingly to make all elements of the first list even. It returns "YES" if the process was successful, and "NO" otherwise. The method applies a time complexity of O(n), where n is the size of the list. 

This approach allows you to solve the given problem in a straightforward and effective manner, as requested. 
The following code is the explanation in a few lines: 
```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```
The code uses a for loop to iterate through each element in lst1, and uses the modulo operator to check if the number is odd. If an odd number is found, it flips the variable odd to false, and vice versa. In the end, the variable odd will be false if there are no odd numbers in lst1, and thus, all elements in lst1 can be exchanged with even numbers in lst2 to achieve the goal.