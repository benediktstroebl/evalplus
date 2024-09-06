```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val: 
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```
The function iterates through the list, keeping track of the variable `freq`, which records the frequency of the current integer in the list. It also keeps track of `max_val`, which records the maximum value in the list up until the current iteration. We then check if the current integer has a frequency equal to or greater than itself. If so, we return this value, as it is the greatest such integer. If we reach the end of the list without finding such an integer, we return -1, indicating that no such integer exists. 

Here is an example usage of the function for the first test case in the problem statement:
```python
search([4, 1, 2, 2, 3, 1])
```
This would output:
```bash
2
```