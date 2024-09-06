```python
def unique(l: list):
    seen = set()
    result = []
    for x in l:
        if x not in seen:
            seen.add(x)
            result.append(xunique)
   return []
all(unique(test_list) == [0, 2, 3, 5, 9, 123])
``` 
This function `unique` takes a list as input and uses a set to keep track of the unique elements seen so far. The function then iterates through the elements in the list and adds them to the set. Finally, it creates a new list with the unique elements and returns it. 

The test passed to the function is a list of numbers, and it should return a list of numbers that are also in the original list.