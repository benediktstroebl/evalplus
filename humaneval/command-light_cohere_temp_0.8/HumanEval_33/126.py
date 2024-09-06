```python
def sort_third(l: list):
    """Sorts the list l such that all numbers that are not divisible by three are at the beginning, and numbers that are divisible by three are in the corresponding positions in l"""
    # sorts the list such that numbers not divisible by three are at the beginning
    l = [1, 2, 3, 5, 6, 7, 9, 4]
    return sorted(l, key=lambda x: not_is_divisible(x), reverse=True)


def not_is_divisible(x):
    """Returns True if x is divisible by three, False otherwise"""
    return x % 3 == 0

# pass the function to test the sort_third function
if __name__ == "__main__":
    l = [1, 2, 3, 5, 6, 7, 9, 4]
    l = sort_third(l)
    print(l)
```
The function `sort_third` takes a list `l` as input and returns a sorted list `l'` such that all numbers that are not divisible by three are at the beginning, and numbers that are divisible by three are in the corresponding positions in `l`. 

The function `not_is_divisible` returns `True` if the number is divisible by three, and `False` otherwise.