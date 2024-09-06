```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 1:
        return (lst[len(lst)//2][0] + lst[len(lst)//2][1]) / 2
    else:
        return (lst[(len(lst)//2] + 1)[0] + lst[(len(lst)//2) - 1][0]) / 2
```
Do you need any other assistance with writing code or have additional questions related to coding or general knowledge?