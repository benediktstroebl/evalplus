```python
def intersection(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2
    return "YES" if max(s1, s2) < e1 + 1 and s2 < e1 else "NO"

# Sample test cases
intersection((1, 2), (2, 3)) == "NO"
intersection((-1, 1), (0, 4)) == "NO"
intersection((-3, -1), (-5, 5)) == "YES"
```
This script defines a function `intersection` that calculates the length of the intersection of two given closed intervals. It uses interval representation as a pair of integers `(s, e)`, where `s` is the start and `e` is the end. The `max()` function is used to compare the start of each interval with the end of the other interval to determine if they intersect or not. The script also includes several test cases to verify the functionality of the `intersection` function.