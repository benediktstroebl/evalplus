```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [0, ]]

# Test the function with a sample list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # expected output: [0, 2, 3, 5, 9, 123]
``` 
This Python function unique takes a list l as input and uses a set seen to keep track of elements it has encountered so far. It then iterates through desired unique elements from the list and returns them.