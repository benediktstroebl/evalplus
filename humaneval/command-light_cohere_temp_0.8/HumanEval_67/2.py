```python
def fruit_distribution(s,n): 
    """
    Determine and return the total number of mango fruits given the 
    total number of fruits and types of fruits in the basket.
    """
    string temp = s.split(' ')
    particular fruits = s.split(',')[0]. for i in range:
        if i == 'apples':
            temp += int(s.split(',')[1])
        elif i == 'oranges':
            temp += int(s.split(',')[1])
        elif i == 'mango':
            temp += 1
    return temp

#Test cases
test_fruit_distribution = [
    '5 apples and 6 oranges',
    '0 apples and 1 oranges',
    '2 apples and 3 oranges',
    '100 apples and 1 oranges',
    '120 apples and 1 oranges',
    '3 apples and 30 oranges',
    '10 apples and 20 oranges',
    '100 apples and 20 oranges',
]

for i,test in enumerate(test_fruit_distribution):
    result = fruit_distribution(test,len(test_fruit_distribution))
    print(test,':',result)
```