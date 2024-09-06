```python
def unique(l: list):
    seen = set()
    result = []
    for x in l:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

#Test the function
test_result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_result)
``` 
The function unique takes a list l as input and returns a new list with unique elements from l. It uses the fact that all unique elements are added to a set, and then the set is converted back into a list of unique elements. The list of unique elements is then returned as the result of the function.