```python
def is_sorted(lst):
    # Count the unique elements and sort the list if it contains multiple unique elements
    if len(set(lst)) > 1 and lst != sorted(lst):
        return False
    # Check if the list has duplicate elements by iterating and verifying if each element's next element is greater
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True
```

This function works by using two nested conditions to verify the list's properties. The first condition checks if the list has more than one unique element, and if so, it sorts the list to ensure a consistent check mechanism. The second condition checks if any elements are not greater than the previous element, returning False if any are found. If both conditions are passed, the function returns True. 

This effectively solves the problem while maintaining a concise and efficient implementation. Let me know if you'd like me to explain any part of the code further.