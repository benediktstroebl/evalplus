```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case where we would exceed the list bounds, just append the remaining element(s) to the list
            l_new.extend(l[i:i+3])
    return l_new
```
This script takes a list `l` and returns a list `l_new` that follows the requirements outlined in the problem prompt. It steps through the list in increments of three and sorts the subsequent triplets. If for some reason a triplet is not present (e.g. list length is not divisible by three), it will handle it by directly appending these elements to `l_new`. Enjoy coding and testing this solution further! Let me know if you have any other questions.