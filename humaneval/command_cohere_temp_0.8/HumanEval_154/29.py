```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    
    rotations = [second, second[1:] + second[:1], second[2:] + second[:2]]
    
    return any(second in first for second in rotations)
```

This code works by first creating a list of rotated versions of the second word, then checking each one against the first word (ignoring case). Any rotation that's a substring of the first word leads to a return value of True, while if no rotations match, the function returns False. 

This approach ensures the function is resilient to variations in letter casing and doesn't require any external dependencies. 
If you would like to test this function against different permutations and combinations, feel free to ask for more test cases.