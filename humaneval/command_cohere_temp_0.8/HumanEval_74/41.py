```python
def total_match(lst1, lst2):
    l1,l2 = len(lst1[0]), len(lst2[0])
    for i in range(min(len(lst1), len(lst2))):
        if l1 + l2 - 2*(i+1) < l2:
            return lst1
        if l2 + l1 - 2*(i+1) < l1:
            return lst2
    if l1 <= l2:
        return lst1
    return lst2
``` 

The solution utilizes the fact that the returns the shorter list based on the cumulative count of characters in the strings in the list, the algorithm keeps track of the length of the i-th string in the list (l1 and l2) and uses the formula : `cumulativeCount(currentList) = cumulativeCount(otherList) + (length of string in currentList) - (2*(current list index + 1))`. At each step the algorithm compares which cumulative count is less and returns the corresponding list. In case the cumulative counts are the same for both lists, the algorithm returns `lst1` since it was the first list to begin with.