```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two fruits' counts as integers using **map()** and saves them as **apples** and **oranges** with **split()** on the **' and '** string. Then it's just a matter of returning the total count for the basket **n** minus the counts for the apples and oranges. 

Here is a test case to validate the code:
```python
print(fruit_distribution("7 apples and 8 oranges",23))
```
Which should output:
```bash
8
```

Such that the total count of the basket is 23, and 7 apples and 8 oranges were present, making 23 - 7 - 8 = 8 mango fruits in the basket.