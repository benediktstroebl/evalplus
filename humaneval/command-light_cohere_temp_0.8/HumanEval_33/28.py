```python
def sort_third(lst):
    # code to sort list of numbers not divisible by three
    return sorted(lst, key=lambda x:int(x)//3 if x%3 else x)

# test cases
print("Test Case 1: ",sort_third([1, 2, 3]))   
print("Test Case 2: ",sort_third([5, 6, 3, 4, 8, 9, 2]))
print("Test Case 3: ",sort_third([10, 20, 30])) 
``` 
This script defines a function `sort_third` that sorts a list of numbers in a way that numbers not divisible by three stay in their original order, while numbers divisible by three are sorted to be equal to their original values.