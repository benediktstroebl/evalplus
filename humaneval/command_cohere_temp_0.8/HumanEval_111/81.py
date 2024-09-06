```python
def histogram(test):
    letters = test.strip().lower().split()
    count = {}
    for letter in letters:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count
```
The function creates a dictionary called `count`, where the keys are single lowercase letters, and the values are the number of times that letter appears in `letters`. The keys with equal values are retained, thereby, if several letters have the same occurrence, the function will return all of them. 

This approach guarantees the proper working of the function against the mentioned tests.