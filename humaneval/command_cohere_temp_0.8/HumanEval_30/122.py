```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension to filter out elements that are not positive numbers, offering a clean and concise solution. 

Such a concise approach employs a plain for loop and an if condition to achieve the same result:
```python
def get_positive(l: list):
    positive_numbers = []
    for num in l:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers
```

You can confidently use either of these approaches to solve the problem and fulfill the requirement of extracting only positive numbers from a given list.