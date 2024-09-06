```python
def unique(l: list):
    seen = set()
    result = []
    for num in l:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
``` 
This code defines a function named `unique` that takes a list `l` as input and returns a new list containing unique elements from the input list. The function uses a set to keep track of seen elements, then iterates through the input list and appends each unique element to the result list. This ensures that duplicate elements are excluded from the final result.