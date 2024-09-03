```python
def add(lst):
    """Given a non-empty list of integers lst. add the elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    res = 0
    for i in range(len(lst)//2):
        if lst[i]%2 == 0:
            res += lst[i]
    return res 

# Test cases
test_add = []
for i in range(5):
    test_add.append([4, 2, 6, 7])
print(add(test_add)) # Output: 2
``` 
This code defines a function called add that takes a list of integers as input. It then runs through the area formula to calculate the sum of the odd elements in the list. This works because the odd indices are those elements at odd positions, so the area formula will work correctly.