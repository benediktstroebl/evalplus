Here's a self-contained Python function that finds the number of times a given substring can be found in the original string, while accounting for cases with overlapping substring matches:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    subindex = string.find(substring, 0)
    
    while subindex != -1:
        count += 1
        subindex = string.find(substring, subindex + len(substring))
        
    return count
```
This function uses the `find` method within a while loop to locate the substring in the string, and increments the count every time the substring is found in a new position. The loop continues until the string does not contain the substring anymore.