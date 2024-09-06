```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    second = second.replace(" ","")
    second = second.strip(".")
    second = second.strip("!")
    second = second.strip("?")
    
    rotations = [second[i:]+second[:i] for i in range(len(second))]
    rotations = [x for x in rotations if x]
    return any(second in first or x in first for x in rotations)
```