```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. Whether each element in the list appears only once (using the dictionary `dups`).
2. Whether each element is less than its subsequent appearance(s), if any (using the dictionary `dups`). 

This solution leverages Python's concise and expressive nature to solve the problem succinctly while maintaining clarity. Let's break down the code step by step:
1. **Defining the Function**:
   ```python
   def is_sorted(lst):
   ```
   Here, we're defining a function named `is_sorted` that takes a single argument `lst`, which is the list of numbers we want to analyze.
2. **Duplicate Check**:
   ```python
   dups = {}
   for num in lst:
       if num in dups:
           dups[num] += 1
       else:
           dups[num] = 1
   ```
   A dictionary named `dups` is initialized to store the occurrences of each number in the list. The loop iterates through each number in the input list. If the number is already present in the dictionary, its count is incremented; otherwise, it's added to the dictionary with a count of 1.
3. **Test for Uniqueness**:
   ```python
   return all(dups[num] == 1 for num in dups)
   ```
   This line checks whether each number in the list appears exactly once (i.e., no duplicates). The `all` function iterates through each key in the `dups` dictionary and verifies that every value is equal to 1, indicating no duplicates.
4. **Test for Sorting**:
   ```python
   and all(num < nums[1] for num, nums in dups.items())
   ```
   This line checks whether the numbers in the list are sorted. The `and` operator combines this condition with the uniqueness condition checked earlier. For each number, it compares it with the next occurrence of that number (indexed as `nums[1]`) in the `dups` dictionary to ensure sorting.

The function returns `True` if both conditions are met (no duplicates and sorting), and `False` otherwise.

This solution is characteristic of efficient Python practices, leveraging dictionaries and concise syntax, and provides an effective way to solve the problem.