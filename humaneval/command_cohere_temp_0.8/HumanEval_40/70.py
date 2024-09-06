```python
def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    cnt = Counter(lst)
    
    # Filtering for elements that appear exactly twice in the list
    twice_ occurring = [k for k, v in cnt.items() if v == 2]

    # Using a list comprehension to check if the sum of each trio is zero
    return any(sum(el >= 0 and el <= 0 for el in zip(thrice, twice_)) == 0 for twice, thrice in zip(twice_occurring, lst, lst))
```

The function uses a Counter class to count the occurrences of each element in the list. Then it filters the elements that appear exactly twice and uses a list comprehension to check if the sum of each trio is zero. The function returns True if there is a trio that sums up to zero and False otherwise. It is important to mention that the order of the list is important to make the sum of the trio equal to zero. You can use the function by calling it and passing a list as an argument like this:
```python
print(triples_sum_to_zero([1, 3, 5, 0])) # Output: False
``` 
This example will print `False` because there is no trio in the list that sums up to zero.