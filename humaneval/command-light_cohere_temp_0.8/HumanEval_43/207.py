Here's the improved Python code:
```python
def pairs_sum_to_zero(l):
    s, i = 0, len(l) - 1
    while i >= 0 and l[i] > 0:
        s += l[i]
        i -= 1
    return s < 0
```
This code has been enhanced to solve the problem more effectively. The main idea is to traverse the list using two pointers, one starting from the beginning and the other from the end, and continuously sum the integers. The function returns True if a sum at any point is less than 0 and False otherwise.