```python
def sort_third(lst):
    # list comprehension to filter out numbers divisible by 3
    divisible = [num for num in lst if num % 3 == 0]
    
    # sorting remaining elements
    return sorted(set(l for l in lst if l not in divisible))

# Test cases
print(sort_third([1, 2, 3]))       # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 20, 30, 40, 50, 60, 20])) # [30, 40, 50, 60, 20, 10]
```