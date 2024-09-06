```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Run the function and print the result
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
 ``` 
This code defines a function called unique that takes a list as input and returns a new list containing only the unique elements from the input list. The function uses a set to keep track of the unique elements and a list to build the result. It then iterates through list and adds each element to the result list if it is not already in the seen set. Finally, it returns the result.