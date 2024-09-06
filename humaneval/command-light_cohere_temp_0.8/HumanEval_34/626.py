```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print("Unique list:", result)

test_set = set(test_list)
print("Set:", test_set)

test_list2 = list(map(int,input("input ").split()))
result = unique(test_list2)
print("Unique list:", result)
``` 
This Python code defines a function called unique that takes a list as input and aims to return a list of unique elements from that list. It uses a seen = set() to keep track of elements that have been encountered, and it initializes an empty list result to hold the unique elements. The code then iterates through each element in the input list and checks if it's not already in the seen set. If it's not, it adds the element to the seen set and appends it to the result list. Then, it returns the list of unique elements.

The code also provides some test cases: it creates a list test_list, calls the unique function with this list, and prints the result. It also converts the input into a set, which should contain all the unique elements from the original input list. Finally, it creates a new list, passes it to the unique function, and prints the result.