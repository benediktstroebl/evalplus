```python
def sort_third(lst):
    """This function sorts a list l such that elements not divisible by three are at the beginning"""
    return sorted(lst, key=lambda x: not_divisible(x))
   
    # This lambda function checks if a number is divisible by three
    def not_divisible(x):
        return x % 3 == 0
```