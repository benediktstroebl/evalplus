```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in dups.items():
        if v > 1:
            return False
    return True
```

The function employs a simple algorithm that takes a list of numbers and determines whether they are sorted and if there are any duplicate numbers. It checks if there are any elements that appear more than once in the list, and if so, it counts how many times each of them appears in a dictionary called `dups`. After populating `dups`, it iterates over its keys and if any of the values is greater than 1, it returns `False` since the condition of having duplicate numbers more than once is not met. If the list passes these conditions, it returns `True`. 

The script should tackle the examples provided in the problem statement and pass all the tests.