```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the total number of fruits in the basket as a parameter and then separates the number of apples and oranges by their names in the `string` s and returns the number of mangoes based on the formula `n - apples - oranges`. 

---|---
| **Code** | **Explanation** |
|---|---|
| 1 | `apples, oranges = map(int, s.split(' and '))` |
| - | This line uses the `split` method to separate the string `s` into two strings representing the number of apples and oranges using the `and` as the separator. |
| - | `apples, oranges = map(int, ['apples', 'oranges'])` |
| - | This line uses the `map` function to convert the two strings into integer numbers of apples and oranges. |
| 2 | `return n - apples - oranges` |
| - | This line uses the formula for solving the problem and returns the number of mangoes, subtracting the number of apples and oranges from the total number of fruits in the basket. |

The approach taken in this solution is **Dynamically Programming** with a **Brute Force** **Solution** and it takes **O(1)** or **Constant Time** to perform the operation.