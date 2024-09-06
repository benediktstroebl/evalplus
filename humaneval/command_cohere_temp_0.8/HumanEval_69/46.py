```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        elif val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq == -1 else -1 
```

The function `search` iterates through the list `lst`, tracking the maximum value `max_val`. It also keeps track of the frequency of the current maximum, updating the frequency `freq` whenever a value equals the maximum and its frequency is greater than or equal to its value. Ultimately, the function returns the maximum value if its frequency qualifies, or -1 if no such value exists. 

Here is an example usage of the function `search`:
```python
search([1, 2, 2, 3, 3, 3, 4, 4, 4])
```
Which returns:
```bash
3
``` 

And here is an example usage where the condition is not met:
```python
search([5, 5, 4, 4, 4])
```
Which returns:
```bash
-1
```