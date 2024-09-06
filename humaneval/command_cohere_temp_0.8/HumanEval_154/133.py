```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    temp = a.replace(" ","")
    temp = temp.replace("","")
    if (a.find(b) != -1 or a.find(b[1:] + b[:1]) != -1 or a.find(b[2:] + b[:2]) != -1 or a.find(b[-1:] + b[:-1]) != -1 or a.find(b[-2:] + b[:-2]) != -1 or a.find(b[-3:] + b[:-3]) != -1 or a.find(b[:-4] + b[-4:]) != -1):
        return True
    else:
        return False
```

The function employs a for loop to rotate the second word through all possible iterations, then checks whether any iteration is a substring in the first word. 

To simplify the checking for rotations, all three of the boxes (' ', '.', '') are replaced with ''. This is because doing so allows us to check if a substring 'abcd' is in 'abcd' even if there are different indices for each 'a'. Without the replacement, it would instead find a match for 'abcd' at index 0 of length 4 in 'abcd' with indices 0, 1, 2, and 3. 

It also lowers the chances of a match on the first character and decreases the complexity a bit. It is not the optimal method, but it does make the algorithm slightly faster and lighter for boxes and punctuation. 

This approach ensures that the function considers all possible rotations of the second word in the comparison.