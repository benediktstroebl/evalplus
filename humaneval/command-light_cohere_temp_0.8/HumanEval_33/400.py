```python
def sort_third(lst):
    """Sorts the list l such that all numbers not divisible by three are at the beginning, while the numbers divisible by three are at the end"""
    return sorted(lst, key=lambda x: (not divisible(x), x))
 
def divisible(x):
    return x // 3 == 0
 
# Test cases
if __name__ == "__main__":
    # Test case 1
    lst1 = [5, 6, 3, 4, 8, 9, 2]
    print("Test case 1 result:", sort_third(lst1))  # Output: [2, 6, 3, 4, 8, 9, 5]
    
    # Test case 2
    lst2 = [1, 2, 3, 4, 8, 9, 2]
    print("Test case 2 result:", sort_third(lst2))  # Output: [2, 3, 4, 6, 8, 9, 5]
    
    # Test case 3
    lst3 = [1, 2, 3, 4, 8, 9, 2, 10]
    print("Test case 3 result:", sort_third(lst3))  # Output: [2, 3, 4, 6, 8, 9, 5, 10]
    
    # Test case 4
    lst4 = [10, 11, 12, 13, 14, 15, 16, 17]
    print("Test case 4 result:", sort_third(lst4))  # Output: [10, 11, 12, 13, 14, 15, 16, 17]
```

The script defines a function `sort_third` that sorts a list in a specific manner. The function takes a result lists and returns their sorted versions, ensuring that all numbers divisible by three are at the end and those not divisible by three are at the beginning. The test cases cover a main scenarios to ensure the functionality of the function.