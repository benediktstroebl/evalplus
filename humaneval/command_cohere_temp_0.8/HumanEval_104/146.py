```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to filter out elements that have at least one even digit. The function then returns the filtered list sorted in increasing order. 

The basic logic behind the function is to use a list comprehension that loops through each element in the list. For each element, it checks if any digit of that element is even. If there are no odd digits, it adds that element to the new list. The function returns the new list as the output.